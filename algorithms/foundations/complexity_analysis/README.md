# Complexity Analysis (Big-O)

> Status: ✅ Complete

Part of the [DSA curriculum](../../../CURRICULUM.md) — Phase 0 - Foundations.

## What you'll learn

- Why we measure algorithms instead of just "seeing if they work"
- What Big-O notation means and how to read it
- How to analyze the **time** and **space** cost of a piece of code
- The common complexity classes, from fastest to slowest
- Best, average, and worst case — and which one usually matters

---

## Why this matters

Two programs can both produce the correct answer, yet one finishes in a second and the other takes a week. The difference isn't the hardware — it's how the amount of work **grows** as the input gets bigger.

For 10 items, almost anything is fast. For 10 million items, only the right approach survives. Complexity analysis lets us predict that *before* running the code.

---

## The core idea

Big-O answers one question:

> **As the input size `n` grows, how does the amount of work grow?**

Key points:

- It ignores exact seconds, CPU speed, and programming language.
- It cares about the **shape** of the growth curve, not exact counts.
- `n` means *the size of the input* (length of a list, number of nodes, etc.).

**Analogy:** Imagine traveling to a city. "It takes about 2 hours" is like exact runtime. "It grows proportionally with the distance" is like Big-O — a statement about how the cost scales.

---

## The three rules

1. **Drop constants.** `2n` → `O(n)`, `1000n` → `O(n)`. Constants don't change the shape of a line.
2. **Drop lower-order terms.** `n² + n + 5` → `O(n²)`. For large `n`, the `n²` term dominates completely.
3. **Different inputs get different variables.** A loop over `a` then a loop over `b` is `O(a + b)`, **not** `O(n)`. Only call it `n²` if both loops are over the *same* `n`.

---

## Common complexity classes (cheat sheet)

| Notation | Name | Example | Work at n = 1,000 |
|----------|------|---------|-------------------|
| `O(1)` | Constant | Access `items[0]` | 1 |
| `O(log n)` | Logarithmic | Binary search, halving | ~10 |
| `O(n)` | Linear | Sum a list, linear search | 1,000 |
| `O(n log n)` | Linearithmic | Merge sort, quick sort (average) | ~10,000 |
| `O(n²)` | Quadratic | All pairs, bubble sort | 1,000,000 |
| `O(2ⁿ)` | Exponential | Naive recursive Fibonacci | astronomically large |
| `O(n!)` | Factorial | Trying every permutation | unimaginably large |

The first four are your friends. Anything above `O(n²)` becomes unusable quickly.

> **Note:** The base of a logarithm doesn't matter in Big-O — `log₂n` and `log₁₀n` differ only by a constant factor, and we drop constants.

---

## Best, average, and worst case

Consider searching for a value in an **unsorted** list:

- **Best case:** it's the first item → `O(1)`
- **Average case:** it's around the middle → `O(n)` (technically ~n/2)
- **Worst case:** it's last, or not present → `O(n)`

When someone says "the complexity of X" without qualification, they usually mean the **worst case** — it's the guarantee you can rely on.

---

## Time vs. space

- **Time complexity:** how the amount of *work* grows.
- **Space complexity:** how the *extra memory* grows.

```python
def sum_items(items):        # O(n) time
    total = 0                # O(1) extra space — one variable
    for value in items:
        total += value
    return total

def copy_items(items):       # O(n) time  (must touch every item)
    return list(items)       # O(n) extra space — the copy grows with input
```

A common trade-off: using **more memory** to get **less time** (e.g., a hash table).

---

## How to analyze code (step by step)

1. **Identify the input size `n`.**
2. **Find the loops or recursive calls.**
3. **Count operations in terms of `n`.** Nested loops multiply; sequential loops add.
4. **Apply the rules:** drop constants and lower-order terms.
5. **State the worst case** (and time vs. space if both are relevant).

---

## Worked examples

### Example 1 — Constant `O(1)`

```python
def first(items):
    return items[0]       # one access, even for a billion items
```

### Example 2 — Linear `O(n)`

```python
def total(items):
    s = 0
    for x in items:       # runs n times
        s += x
    return s              # -> O(n)
```

### Example 3 — Quadratic `O(n²)`

```python
def pairs(items):
    for i in items:        # n times
        for j in items:    # n times for EACH i -> n x n
            print(i, j)    # -> O(n²)
```

### Example 4 — Logarithmic `O(log n)`

```python
while n > 1:
    n //= 2                # halving n each step
                           # n=1024 -> 512 -> 256 -> ... -> 1 (10 steps)
```

Halving is the signature of `O(log n)`. Doubling the input adds only **one** extra step.

### Example 5 — Linearithmic `O(n log n)`

Merge sort does `n` units of work at each of `log n` levels → `n × log n`. This is the best you can do for comparison-based sorting.

---

## Common mistakes

- **Confusing `n` with a value.** The input `[5000]` has size 1, not 5000.
- **Thinking `O(n)` means exactly `n` operations.** It means "grows linearly" — `3n + 7` is still `O(n)`.
- **Ignoring hidden costs.** `x in some_list` is `O(n)` (linear scan); `some_list[i]` is `O(1)`. Slicing copies data → `O(n)`.
- **Counting the wrong thing.** State clearly whether you're analyzing time, space, best, or worst case.

---

## When to use it

- Choosing between two algorithms before coding either
- Spotting why code is slow on large inputs (usually an accidental `O(n²)`)
- Communicating performance clearly with other developers
- Technical interviews — this is the universal language of algorithms

---

## Files in this folder

| File | What it's for |
|------|---------------|
| `implementation.py` | Reference functions for each complexity class, with an optional operation counter |
| `example.py` | Run `python example.py` to see operation counts grow as `n` grows |
| `exercises.py` | Your turn: implement functions with a target complexity + written questions |
| `solution.py` | Worked solutions (try the exercises first!) |
| `test_topic.py` | `python -m unittest test_topic.py` to verify correctness **and** operation counts |

Try the exercises before opening `solution.py`, then run the tests.
