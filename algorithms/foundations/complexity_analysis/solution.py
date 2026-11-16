"""Worked solutions to the exercises in exercises.py.

Try the exercises yourself first — peek here only when stuck.
"""

from exercises import (  # noqa: F401 — re-exported for convenience
    exercise_1_sum_loop,
    exercise_2_sum_formula,
    exercise_3_pairs,
    exercise_4_halvings,
)


def solve_exercise_1_sum_loop(n):
    """O(n): one loop, n iterations."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def solve_exercise_2_sum_formula(n):
    """O(1): Gauss's formula n(n+1)/2 — no loop, fixed number of operations."""
    return n * (n + 1) // 2


def solve_exercise_3_pairs(items):
    """O(n^2): nested loops, ~n^2/2 pairs. We write O(n^2) (drop constants)."""
    pairs = []
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((items[i], items[j]))
    return pairs


def solve_exercise_4_halvings(n):
    """O(log n): each step halves n, so we take ~log2(n) steps."""
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps


# ---------------------------------------------------------------------------
# Answers to written questions
# ---------------------------------------------------------------------------
# Q1. Big-O describes growth RATE, not exact counts. Constants don't change
#     the shape of the curve; 2n and n both grow linearly.
# Q2. O(n): the inner loop runs a constant 3 times, so total work is 3n -> O(n)
#     after dropping the constant.
# Q3. Best O(1) (found first), average O(n) (~n/2), worst O(n) (last or absent).
# Q4. Changing log base only multiplies by a constant
#     (log2(n) = log10(n) / log10(2)), and we drop constants in Big-O.
