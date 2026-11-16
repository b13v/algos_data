# algos_data

A hands-on, from-scratch study of **Data Structures and Algorithms** in Python.

This repo is structured as a guided course: each algorithm and data structure gets its own folder with a complete "learning kit" (explanation, annotated code, runnable example, exercises, solutions, and tests). We work through topics one at a time, in order.

## Start here

- **[CURRICULUM.md](CURRICULUM.md)** — the full learning plan, topic order, and progress tracker.

## Repo layout

```
algos_data/
├── CURRICULUM.md          # the learning roadmap (start here)
├── README.md              # this file
├── templates/topic/       # blank starter kit for new topics
├── algorithms/            # sorting, searching, recursion, graphs, etc.
│   └── README.md
└── data_structures/       # arrays, lists, stacks, trees, graphs, etc.
    └── README.md
```

## Anatomy of a topic

Every topic folder follows the same template (`templates/topic/`):

| File | Purpose |
|------|---------|
| `README.md` | Intuition, walkthrough, complexity table, when to use it |
| `implementation.py` | Clean, annotated reference implementation |
| `example.py` | Runnable demo |
| `exercises.py` | Practice problems with `TODO` stubs |
| `solution.py` | Worked solutions |
| `test_topic.py` | `unittest` tests |

## Running the code

```bash
# run a topic's demo (from inside that topic folder)
python example.py

# run the tests for a topic
python -m unittest test_topic.py
```

No third-party dependencies are required — everything uses the Python standard library.
