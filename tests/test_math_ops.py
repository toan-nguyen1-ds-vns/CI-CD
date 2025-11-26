import os
import sys
import pytest

"""Tests for math_ops.

The tests may read `FIST` and `SECOND` from the environment. To make local
and CI runs robust we read them with `os.environ.get` and provide sensible
defaults, then cast to int.
"""

fist = int(os.environ.get("FIST", "0"))
second = int(os.environ.get("SECOND", "0"))
# Ensure `src` directory is on sys.path so tests can import `math_ops` without an install.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from math_ops import add, subtract, sum_list


def test_add_integers():
    assert add(fist, second) == 4


def test_subtract_integers():
    assert subtract(second, fist) == 4


def test_add_floats():
    assert add(2.5, 0.5) == 3.0


def test_sum_list_nonempty():
    assert sum_list([1, 2, 3, 4]) == 10


def test_sum_list_empty():
    assert sum_list([]) == 0


def test_sum_list_invalid_input():
    with pytest.raises(TypeError):
        sum_list(None)
