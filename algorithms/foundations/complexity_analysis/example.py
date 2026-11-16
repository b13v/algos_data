"""Runnable demo: watch operation counts grow with input size.

Run with: python example.py
"""

from implementation import (
    Counter,
    constant_time,
    linear_time,
    quadratic_time,
    logarithmic_time,
    linearithmic_time,
    linear_space,
)

SIZES = [1, 2, 4, 8, 16, 32, 64]


def measure(fn, size, uses_list):
    counter = Counter()
    data = list(range(size))
    fn(data if uses_list else size, counter=counter)
    return counter.count


def main():
    print("OPERATION COUNTS AS INPUT SIZE n GROWS")
    print("(each function counts its own basic operations)\n")

    header = (
        f"{'n':>6} | {'O(1)':>8} {'O(log n)':>10} {'O(n)':>8} "
        f"{'O(n log n)':>12} {'O(n^2)':>10}"
    )
    print(header)
    print("-" * len(header))
    for n in SIZES:
        c = measure(constant_time, n, True)
        log = measure(logarithmic_time, n, False)
        lin = measure(linear_time, n, True)
        nlogn = measure(linearithmic_time, n, False)
        quad = measure(quadratic_time, n, True)
        print(f"{n:>6} | {c:>8} {log:>10} {lin:>8} {nlogn:>12} {quad:>10}")

    print("\nNOTICE:")
    print("  - O(1)      stays at 1 no matter how big n gets")
    print("  - O(log n)  grows by just +1 each time n doubles")
    print("  - O(n)      doubles when n doubles")
    print("  - O(n log n) grows slightly faster than O(n)")
    print("  - O(n^2)    QUADRUPLES when n doubles  <-- watch this explode")

    print("\nSPACE COMPLEXITY (extra memory used):")
    for n in [1, 10, 1000]:
        data = list(range(n))
        space_used = len(linear_space(data))
        print(f"  n={n:>5}: constant_space -> O(1) (one accumulator), "
              f"linear_space -> {space_used} extra items")

    print("\nCHEAT SHEET (growth at n = 1,000):")
    print("  O(1)        1")
    print("  O(log n)    ~10")
    print("  O(n)        1,000")
    print("  O(n log n)  ~10,000")
    print("  O(n^2)      1,000,000")
    print("  O(2^n)      astronomically large")


if __name__ == "__main__":
    main()
