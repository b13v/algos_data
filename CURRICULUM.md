# Data Structures & Algorithms — Learning Curriculum

This is your roadmap for learning Data Structures and Algorithms (DSA) from scratch using Python. It is designed for a complete beginner: every concept is explained from first principles, with plenty of runnable examples and exercises.

> **How this repo works:** We study **one topic at a time**, in the order below. Each topic lives in its own folder and follows the same "learning kit" layout, so once you learn the rhythm, you can focus on the ideas rather than the file structure.

---

## 1. How to use this repo

1. Open `CURRICULUM.md` (this file) and find your current phase.
2. Go into that topic's folder and read its `README.md` — the concept explanation and complexity analysis.
3. Run `python example.py` to see the algorithm in action.
4. Read `implementation.py` line by line (it is heavily annotated).
5. Try the problems in `exercises.py` yourself before peeking at `solution.py`.
6. Run `python -m pytest test_topic.py` to check your work.
7. Mark the topic done in the **Progress tracker** at the bottom of this file, then move on.

Each topic folder contains:

| File | Purpose |
|------|---------|
| `README.md` | Intuition, step-by-step walkthrough, complexity table, when to use it |
| `implementation.py` | Clean, annotated reference implementation |
| `example.py` | Runnable demo showing the algorithm/data structure in action |
| `exercises.py` | Practice problems with `TODO` stubs for you to fill in |
| `solution.py` | Worked solutions to the exercises |
| `test_topic.py` | `pytest` tests that verify correctness |

A blank starter kit is available in `templates/topic/` — copy it to begin a new topic.

---

## 2. The roadmap

### Phase 0 — Foundations
*Goal: understand how to measure an algorithm before writing one.*

| # | Topic | Folder | You'll learn |
|---|-------|--------|--------------|
| 0.1 | Complexity Analysis | `algorithms/foundations/complexity_analysis/` | Big-O notation, time vs. space, best/average/worst case, analyzing loops |

### Phase 1 — Sorting & Searching
*Goal: understand the classic algorithms and how to compare them.*

| # | Topic | Folder | Key idea |
|---|-------|--------|----------|
| 1.1 | Bubble Sort | `algorithms/sorting/bubble_sort/` | Repeatedly swap adjacent out-of-order items |
| 1.2 | Selection Sort | `algorithms/sorting/selection_sort/` | Repeatedly pick the smallest remaining item |
| 1.3 | Insertion Sort | `algorithms/sorting/insertion_sort/` | Build a sorted prefix one item at a time |
| 1.4 | Merge Sort | `algorithms/sorting/merge_sort/` | Divide, sort, then merge (divide & conquer) |
| 1.5 | Quick Sort | `algorithms/sorting/quick_sort/` | Partition around a pivot, then recurse |
| 1.6 | Heap Sort | `algorithms/sorting/heap_sort/` | Sort using a binary heap |
| 1.7 | Counting Sort | `algorithms/sorting/counting_sort/` | Count occurrences instead of comparing |
| 1.8 | Linear Search | `algorithms/searching/linear_search/` | Check each item in order |
| 1.9 | Binary Search | `algorithms/searching/binary_search/` | Halve a sorted array each step |

### Phase 2 — Linear Data Structures
*Goal: understand how data is stored and the cost of common operations.*

| # | Topic | Folder | You'll learn |
|---|-------|--------|--------------|
| 2.1 | Arrays | `data_structures/arrays/` | Indexing, dynamic arrays, insertion/deletion costs |
| 2.2 | Linked Lists | `data_structures/linked_lists/` | Nodes, singly/doubly linked, pointer manipulation |
| 2.3 | Stacks | `data_structures/stacks/` | LIFO, push/pop, call stack applications |
| 2.4 | Queues | `data_structures/queues/` | FIFO, enqueue/dequeue, deque, circular queues |

### Phase 3 — Recursion
*Goal: think recursively and recognize divide-and-conquer.*

| # | Topic | Folder | You'll learn |
|---|-------|--------|--------------|
| 3.1 | Recursion | `algorithms/recursion/` | Base cases, recursive cases, call stack, classic examples |

### Phase 4 — Hashing & Trees
*Goal: understand fast lookup and hierarchical data.*

| # | Topic | Folder | You'll learn |
|---|-------|--------|--------------|
| 4.1 | Hash Tables | `data_structures/hash_tables/` | Hash functions, collisions, load factor, average O(1) lookup |
| 4.2 | Trees | `data_structures/trees/` | Binary trees, BST, in/pre/post-order traversal |
| 4.3 | Heaps | `data_structures/heaps/` | Min/max heap, heapify, priority queues |

### Phase 5 — Graphs
*Goal: model relationships and navigate them.*

| # | Topic | Folder | You'll learn |
|---|-------|--------|--------------|
| 5.1 | Graphs | `data_structures/graphs/` | Vertices, edges, adjacency list vs. matrix |
| 5.2 | BFS | `algorithms/graph_algorithms/bfs/` | Level-by-level traversal, shortest path in unweighted graphs |
| 5.3 | DFS | `algorithms/graph_algorithms/dfs/` | Deep traversal, cycle detection, topological intro |
| 5.4 | Dijkstra | `algorithms/graph_algorithms/dijkstra/` | Shortest path with weighted edges (intro) |

### Phase 6 — Advanced Topics
*Goal: recognize patterns used in harder problems.*

| # | Topic | Folder | You'll learn |
|---|-------|--------|--------------|
| 6.1 | Greedy | `algorithms/greedy/` | Greedy choice property, activity selection |
| 6.2 | Dynamic Programming | `algorithms/dynamic_programming/` | Overlapping subproblems, memoization, tabulation |
| 6.3 | Tries | `data_structures/tries/` | Prefix trees, autocomplete |
| 6.4 | String Algorithms | `algorithms/string_algorithms/` | Pattern matching basics |

---

## 3. How each teaching session works

For every topic, we follow this loop:

1. **Explain** — I fill in the topic's `README.md` and walk you through the intuition.
2. **Show** — We run `example.py` together and trace the output.
3. **Read** — We go through `implementation.py` line by line.
4. **Practice** — You solve `exercises.py` on your own; we compare with `solution.py`.
5. **Verify** — `pytest test_topic.py` must pass before we move on.
6. **Reflect** — You summarize the key idea and its complexity in your own words.

This "learn → do → verify → reflect" loop is what makes the knowledge stick.

---

## 4. Tips for success

- **Don't skip complexity analysis.** Knowing *why* one approach is better is the whole point.
- **Trace code by hand** on small inputs before running it. Draw arrays and pointers.
- **Do the exercises before reading solutions.** Struggling a little is where learning happens.
- **Space repetition:** revisit earlier topics briefly each week.
- **Explain out loud:** if you can teach it simply, you understand it.

---

## 5. Progress tracker

Mark `[x]` when you've completed a topic (README read, example run, exercises done, tests passing).

- [ ] 0.1 Complexity Analysis
- [ ] 1.1 Bubble Sort
- [ ] 1.2 Selection Sort
- [ ] 1.3 Insertion Sort
- [ ] 1.4 Merge Sort
- [ ] 1.5 Quick Sort
- [ ] 1.6 Heap Sort
- [ ] 1.7 Counting Sort
- [ ] 1.8 Linear Search
- [ ] 1.9 Binary Search
- [ ] 2.1 Arrays
- [ ] 2.2 Linked Lists
- [ ] 2.3 Stacks
- [ ] 2.4 Queues
- [ ] 3.1 Recursion
- [ ] 4.1 Hash Tables
- [ ] 4.2 Trees
- [ ] 4.3 Heaps
- [ ] 5.1 Graphs
- [ ] 5.2 BFS
- [ ] 5.3 DFS
- [ ] 5.4 Dijkstra
- [ ] 6.1 Greedy
- [ ] 6.2 Dynamic Programming
- [ ] 6.3 Tries
- [ ] 6.4 String Algorithms
