"""Tests for <Topic Name>.

Run with either:
    python -m unittest test_topic.py      # no install needed (stdlib)
    python -m pytest test_topic.py        # if you have pytest installed
"""

import unittest

from implementation import reference_implementation


class TestTopic(unittest.TestCase):
    def test_example(self):
        self.assertEqual(reference_implementation([1, 2, 3]), [1, 2, 3])

    def test_edge_case_empty(self):
        self.assertEqual(reference_implementation([]), [])


if __name__ == "__main__":
    unittest.main()
