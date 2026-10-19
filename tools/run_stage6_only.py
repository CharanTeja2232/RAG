"""Execute ONLY the Stage 6 cells of RAG_Baseline_vs_Rerank.ipynb, without re-executing Stages 1-5.

The frozen Stage 4-5 state (chunks, preregistered questions, baseline and re-ranked Top-10) is restored from the persisted files after re-checking the
corpus, preregistration and overlay hashes; nothing is re-embedded, re-retrieved or re-ranked. The Stage 6 cells then run in a fresh kernel, their outputs are
written back into the notebook, and the Stage 6 / latency status fields of results/nist_evaluation_manifest.json are refreshed.

    python tools/run_stage6_only.py                                   # mode off: no network, shows what exists
    RAG_STAGE6_MODE=smoke    python tools/run_stage6_only.py          # synthetic prompts only (needs GROQ_API_KEY in the git-ignored .env)
    RAG_STAGE6_MODE=evaluate python tools/run_stage6_only.py          # the 48 evaluation answers; resumable; refuses without a passing smoke test
    python tools/run_stage6_only.py in.ipynb out.ipynb                # optional explicit paths (default: in place, only on success)

The API key is read inside the notebook from the environment / .env and is never printed. Exit code 1 if any cell fails (the notebook is then left untouched).
"""
import copy
import re
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent.parent
src = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "RAG_Baseline_vs_Rerank.ipynb"
out = Path(sys.argv[2]) if len(sys.argv) > 2 else src
nb = nbformat.read(src, as_version=4)

start = next(i for i, c in enumerate(nb.cells) if c.cell_type == "markdown" and c.source.startswith("---\n# Stage N6. Answer generation"))
end = next(i for i, c in enumerate(nb.cells) if c.cell_type == "markdown" and c.source.startswith("## Evaluation manifest and self-test summary"))
all_code = "\n".join(c.source for c in nb.cells if c.cell_type == "code")


def pin(name):
    m = re.search(rf'^{name}\s*=\s*"([0-9a-f]{{64}})"', all_code, flags=re.M)
    assert m, f"{name} is not pinned in the notebook"
    return m.group(1)


PRELUDE = f'''import collections, hashlib, json, os, re, statistics, urllib.request
from pathlib import Path
os.environ.setdefault("HF_HOME", str(Path("data/hf_cache").resolve()))
os.environ["OMP_NUM_THREADS"] = "1"; os.environ["MKL_NUM_THREADS"] = "1"; os.environ["TOKENIZERS_PARALLELISM"] = "false"
OUT_DIR = Path("results"); K_INIT, K_FINAL = 10, 3
FROZEN_CORPUS_SHA256 = "{pin("FROZEN_CORPUS_SHA256")}"
PREREG_SHA256 = "{pin("PREREG_SHA256")}"
OVERLAY_V1_1_SHA256 = "{pin("OVERLAY_V1_1_SHA256")}"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


SELF_TESTS = []


def check(name, cond):
    assert cond, f"SELF-TEST FAILED: {{name}}"
    SELF_TESTS.append(name)


# Restore the frozen state from the persisted files. Hashes are RE-CHECKED; nothing is recomputed, re-embedded, re-retrieved or re-ranked.
CHUNKS = [json.loads(l) for l in open(OUT_DIR / "nist_chunks.jsonl", encoding="utf-8")]
h = hashlib.sha256()
for c in CHUNKS:
    h.update(c["chunk_id"].encode() + b"\\x00" + c["text"].encode("utf-8") + b"\\x01")
assert h.hexdigest() == FROZEN_CORPUS_SHA256, "the frozen corpus changed"
CHUNK_BY_ID = {{c["chunk_id"]: c for c in CHUNKS}}
PRE = json.load(open(OUT_DIR / "nist_preregistration.json", encoding="utf-8"))
assert hashlib.sha256(json.dumps(dict(corpus_sha256=PRE["corpus_sha256"], queries=PRE["queries"]), sort_keys=True, ensure_ascii=False).encode()).hexdigest() == PRE["prereg_sha256"] == PREREG_SHA256, "the preregistration changed"
PREREG_Q = PRE["queries"]
ov = json.load(open(OUT_DIR / "nist_scoring_overlay_v1_1.json", encoding="utf-8"))
assert hashlib.sha256(json.dumps({{k: v for k, v in ov.items() if k not in ("overlay_sha256", "status")}}, sort_keys=True, ensure_ascii=False).encode()).hexdigest() == ov["overlay_sha256"] == OVERLAY_V1_1_SHA256, "overlay v1.1 changed"
BASELINE_PATH, RERANK_PATH = OUT_DIR / "nist_baseline_top10.json", OUT_DIR / "nist_rerank_top10.json"
BASE, RERANK = json.load(open(BASELINE_PATH, encoding="utf-8"))["queries"], json.load(open(RERANK_PATH, encoding="utf-8"))["queries"]
print("Stage 4-5 state restored from the persisted files (corpus, preregistration and overlay hashes re-checked); Stages 1-5 were NOT re-executed.")
'''
FINAL = "update_manifest_stage6()\nprint('manifest: Stage 6 / latency status fields refreshed; every other field untouched')"

tmp = nbformat.v4.new_notebook()
tmp.metadata = copy.deepcopy(nb.metadata)
tmp.cells = [nbformat.v4.new_code_cell(PRELUDE)] + [copy.deepcopy(c) for c in nb.cells[start:end]] + [nbformat.v4.new_code_cell(FINAL)]
for c in tmp.cells:
    if c.cell_type == "code":
        c.outputs, c.execution_count = [], None
failed = None
try:
    NotebookClient(tmp, timeout=3600, kernel_name="python3", resources={"metadata": {"path": str(root)}}).execute()
except Exception as exc:
    failed = f"{type(exc).__name__}: {str(exc)[:400]}"
errors = sum(1 for c in tmp.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.output_type == "error")
if failed or errors:
    side = out.with_suffix(".stage6_failed.ipynb")
    nbformat.write(tmp, side)
    print(f"FAILED ({failed or str(errors) + ' error output(s)'}); the notebook was NOT modified; partial run saved to {side}")
    sys.exit(1)
for k, orig in enumerate(nb.cells[start:end], start):
    ran = tmp.cells[1 + (k - start)]
    if orig.cell_type == "code":
        orig.outputs, orig.execution_count, orig.metadata = ran.outputs, ran.execution_count, ran.metadata
nbformat.validate(nb)
nbformat.write(nb, out)
print(f"executed {end - start} Stage 6 cells (cells {start}-{end - 1}) in a fresh kernel; Stages 1-5 not re-executed; wrote {out}")
