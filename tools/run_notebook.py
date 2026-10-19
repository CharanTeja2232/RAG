"""Execute RAG_Baseline_vs_Rerank.ipynb top to bottom with nbclient (the same thing as Run All) and save the executed notebook.

    python tools/run_notebook.py                                   # default: no network (Stage 6 mode off), executes in place
    RAG_STAGE6_MODE=smoke    python tools/run_notebook.py          # synthetic prompts only; needs GROQ_API_KEY (see README)
    RAG_STAGE6_MODE=evaluate python tools/run_notebook.py          # the 48 evaluation answers; refuses without a passing smoke test; resumable
    RAG_LATENCY_MODE=measure python tools/run_notebook.py          # retrieval / re-ranking latency (about 4 minutes, single-threaded CPU)
    python tools/run_notebook.py notebook.ipynb out.ipynb          # optional: explicit input and output paths

The environment variables are read inside the notebook; this script never sees the API key's value. Exit code 1 if any cell raised an error.
"""
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent.parent
src = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "RAG_Baseline_vs_Rerank.ipynb"
out = Path(sys.argv[2]) if len(sys.argv) > 2 else src
nb = nbformat.read(src, as_version=4)
for cell in nb.cells:
    if cell.cell_type == "code":
        cell.outputs, cell.execution_count = [], None
failed = None
try:
    NotebookClient(nb, timeout=3600, kernel_name="python3", resources={"metadata": {"path": str(root)}}).execute()
except Exception as exc:                                   # a failed run must never overwrite the notebook it started from
    failed = f"{type(exc).__name__}: {str(exc)[:300]}"
errors = sum(1 for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.output_type == "error")
target = out if failed is None and errors == 0 else out.with_suffix(".failed.ipynb")
nbformat.write(nb, target)
print(f"executed {len(nb.cells)} cells; error outputs: {errors}; wrote {target}" + (f"\nFAILED: {failed}" if failed else ""))
sys.exit(1 if failed or errors else 0)
