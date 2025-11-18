# CI-CD
Testing

## pytest demo

This repository now includes a tiny math utility package and pytest tests.

Files added:

- `src/math_ops/__init__.py` - contains `add` and `sum_list` functions.
- `tests/test_math_ops.py` - pytest tests for those functions.
- `requirements.txt` - lists `pytest` for running tests.

To run the tests locally (assuming you have Python and pip available):

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

