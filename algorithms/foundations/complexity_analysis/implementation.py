"""Annotated reference implementations for complexity analysis.

Each function computes a real result AND (optionally) counts its basic
operations through a Counter. The counts let us *see* growth rates instead of
just trusting the math — run example.py to watch it happen.

The ``counter`` argument is purely for teaching. Pass a Counter to instrument
a function, or omit it for normal use.
"""


class Counter:
    """Counts basic operations so we can observe how algorithms scale."""

    def __init__(self):
        self.count = 0

    def tick(self, amount=1):
        self.count += amount

    def __repr__(self):
        return f"Counter({self.count})"


# ---------------------------------------------------------------------------
# O(1) — constant time
# ---------------------------------------------------------------------------
def constant_time(items, counter=None):
    """Return the first item. O(1): one access, regardless of len(items)."""
    if counter:
        counter.tick()
    return items[0]


# ---------------------------------------------------------------------------
# O(n) — linear time
# ---------------------------------------------------------------------------
def linear_time(items, counter=None):
    """Sum the items. O(n): one pass touches each of the n items once."""
    total = 0
    for value in items:
        if counter:
            counter.tick()
        total += value
    return total


# ---------------------------------------------------------------------------
# O(n^2) — quadratic time
# ---------------------------------------------------------------------------
def quadratic_time(items, counter=None):
    """Return every ordered pair. O(n^2): n iterations x n iterations."""
    pairs = []
    n = len(items)
    for i in range(n):
        for j in range(n):
            if counter:
                counter.tick()
            pairs.append((items[i], items[j]))
    return pairs


# ---------------------------------------------------------------------------
# O(log n) — logarithmic time
# ---------------------------------------------------------------------------
def logarithmic_time(n, counter=None):
    """Count how many times n can be halved before reaching 1. O(log n)."""
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
        if counter:
            counter.tick()
    return steps


# ---------------------------------------------------------------------------
# O(n log n) — linearithmic time
# ---------------------------------------------------------------------------
def linearithmic_time(n, counter=None):
    """Model merge sort's work: log n levels, n operations per level."""
    work = 0
    size = n
    while size > 1:
        for _ in range(n):
            if counter:
                counter.tick()
            work += 1
        size //= 2
    return work


# ---------------------------------------------------------------------------
# Space complexity examples
# ---------------------------------------------------------------------------
def constant_space(items):
    """Sum in place. O(1) extra space: one variable, no matter the input."""
    total = 0
    for value in items:
        total += value
    return total


def linear_space(items):
    """Return a copy. O(n) extra space: the copy grows with the input."""
    return list(items)
