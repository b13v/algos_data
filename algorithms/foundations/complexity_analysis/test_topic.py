"""Tests for Complexity Analysis.

Run with either:
    python -m unittest test_topic.py      # no install needed (stdlib)
    python -m pytest test_topic.py        # if you have pytest installed
"""

import unittest

from implementation import (
    Counter,
    constant_time,
    linear_time,
    quadratic_time,
    logarithmic_time,
    linearithmic_time,
    constant_space,
    linear_space,
)
from solution import (
    solve_exercise_1_sum_loop,
    solve_exercise_2_sum_formula,
    solve_exercise_3_pairs,
    solve_exercise_4_halvings,
)


# --- correctness of results -------------------------------------------------
class TestResults(unittest.TestCase):
    def test_constant_time_returns_first_item(self):
        self.assertEqual(constant_time([5, 6, 7]), 5)

    def test_linear_time_sums(self):
        self.assertEqual(linear_time([1, 2, 3, 4]), 10)

    def test_quadratic_time_pair_count(self):
        self.assertEqual(len(quadratic_time([1, 2, 3])), 9)

    def test_logarithmic_time_steps(self):
        self.assertEqual(logarithmic_time(8), 3)

    def test_linearithmic_time_value(self):
        self.assertEqual(linearithmic_time(8), 24)  # 8 * log2(8) = 8 * 3

    def test_space_functions(self):
        data = [1, 2, 3]
        self.assertEqual(constant_space(data), 6)
        copy = linear_space(data)
        self.assertEqual(copy, data)
        self.assertIsNot(copy, data)


# --- operation counts (the whole point of this lesson) ----------------------
class TestOperationCounts(unittest.TestCase):
    def test_constant_time_is_one_operation(self):
        for n in [1, 10, 100]:
            with self.subTest(n=n):
                c = Counter()
                constant_time(list(range(n)), counter=c)
                self.assertEqual(c.count, 1)

    def test_linear_time_is_n_operations(self):
        for n in [1, 10, 100]:
            with self.subTest(n=n):
                c = Counter()
                linear_time(list(range(n)), counter=c)
                self.assertEqual(c.count, n)

    def test_quadratic_time_is_n_squared_operations(self):
        for n in [1, 5, 20]:
            with self.subTest(n=n):
                c = Counter()
                quadratic_time(list(range(n)), counter=c)
                self.assertEqual(c.count, n * n)

    def test_logarithmic_time_operation_count(self):
        for n in [1, 2, 8, 1024]:
            with self.subTest(n=n):
                c = Counter()
                logarithmic_time(n, counter=c)
                self.assertEqual(c.count, n.bit_length() - 1)

    def test_linearithmic_time_operation_count(self):
        for n in [1, 2, 8, 64]:
            with self.subTest(n=n):
                c = Counter()
                linearithmic_time(n, counter=c)
                self.assertEqual(c.count, n * (n.bit_length() - 1))


# --- exercises --------------------------------------------------------------
class TestExercises(unittest.TestCase):
    def test_exercise_1(self):
        self.assertEqual(solve_exercise_1_sum_loop(10), 55)

    def test_exercise_2(self):
        self.assertEqual(solve_exercise_2_sum_formula(10), 55)

    def test_exercise_3(self):
        self.assertEqual(
            solve_exercise_3_pairs([1, 2, 3]),
            [(1, 2), (1, 3), (2, 3)],
        )

    def test_exercise_4(self):
        self.assertEqual(solve_exercise_4_halvings(16), 4)


if __name__ == "__main__":
    unittest.main()
