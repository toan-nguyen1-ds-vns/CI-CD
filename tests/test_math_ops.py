import os
import sys
import pytest

# Ensure `src` directory is on sys.path so tests can import `math_ops` without an install.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from math_ops import add, sum_list


def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    assert add(2.5, 0.5) == 3.0


def test_sum_list_nonempty():
    assert sum_list([1, 2, 3, 4]) == 10


def test_sum_list_empty():
    assert sum_list([]) == 0


def test_sum_list_invalid_input():
    with pytest.raises(TypeError):
        sum_list(None)
