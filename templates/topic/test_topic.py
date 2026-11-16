"""Tests for <Topic Name>.

Run with: python -m pytest test_topic.py
"""

import pytest

from implementation import reference_implementation


def test_example():
    assert reference_implementation([1, 2, 3]) == [1, 2, 3]  # TODO: expected value


def test_edge_case_empty():
    assert reference_implementation([]) == []  # TODO: expected value
