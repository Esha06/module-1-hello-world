# Module 1 Hello World

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Esha06/module-1-hello-world/blob/main/Module_1_Lab.ipynb)

A beginner lab covering Colab, Jupyter notebooks, Python virtual
environments, tests, and a GitHub review and release workflow.

The lab handout and all exercises are in [`Module_1_Lab.ipynb`](Module_1_Lab.ipynb).

## Files

| File | Purpose |
|------|---------|
| `Module_1_Lab.ipynb` | Lab handout + step-by-step Colab notebook |
| `hello.py` | Hello World program (`greet()` function) |
| `test_hello.py` | Unit tests for `greet()` |
| `requirements.txt` | Pinned dependencies (from `pip freeze`) |

## Run locally

1. Create a virtual environment: `python -m venv .venv`
2. Install dependencies using the environment's pip:
   `.venv/bin/python -m pip install -r requirements.txt`
3. Run: `.venv/bin/python hello.py`
4. Test: `.venv/bin/python test_hello.py`

On Windows, use `.venv\Scripts\python.exe` in place of `.venv/bin/python`.

## Release

`v0.1.0` — first release of the Module 1 lab.
