## Bin Packing System with AVL Trees

 

A course project implementing a one-dimensional bin packing system in Python using self-balancing binary search trees (AVL trees) to manage bins and heuristic placement strategies.

## Problem Description

The **bin packing problem** is a classical combinatorial optimization problem where a set of items of varying sizes must be assigned to bins of fixed capacity such that space is used efficiently and the number of bins used is minimized. This problem is known to be NP-hard in the general case.  [oai_citation:0‡Wikipedia](https://en.wikipedia.org/wiki/Bin_packing_problem?utm)

## Approach

This implementation uses the following verified techniques:

- **AVL Tree for Bin Management:** Bins are maintained in a self-balancing binary search tree keyed by remaining capacity to support efficient search, insertion, and deletion as objects are packed or bins are updated.
- **Heuristic Placement Strategies:**
  - **Smallest Fit:** For each object, find the smallest bin that can accommodate it to reduce wasted capacity.
  - **Largest Fit:** As an alternative, place objects into the largest available bin that fits, which may be useful under certain distributions of object sizes.

Custom exceptions handle basic error conditions such as an object that cannot fit in any existing bin.

> No neural networks, reinforcement learning, or external solvers are used; this is a heuristic, deterministic Python implementation.

## Repository Structure

- `main.py` — Entry point that orchestrates input parsing and the bin packing process.
- `bin.py` — Definition of the `Bin` class, representing a bin with capacity and packed objects.
- `object.py` — Definition of the `Object` class and ancillary enums (e.g., color).
- `avl.py` — Implementation of the AVL tree structure used to manage bins.
- `node.py` — Node abstraction for the AVL tree encapsulating a bin.
- `exceptions.py` — Custom exception types used to signal packing errors.
- `gcms.py` — Auxiliary functions for memory or object lifecycle management (as inferred from project summary).

## How to Run

1. Ensure Python 3.x is installed.
2. Place input data (objects and bins) in the expected format as required by `main.py`.
3. Run:

```bash
python main.py'''

4. The output reflects the bins used and how objects are packed into each bin.

**Note:**  
The repository does not define a formal command-line interface. You may need to adapt `main.py` to suit specific input formats or testing requirements.

---

## Complexity Analysis

### Data Structures

- **AVL Tree Operations**
  - Search, insert, and delete operations each run in `O(log n)` time, where `n` is the number of bins.
  - This efficiency is guaranteed by the height-balanced property of AVL trees.

### Algorithms

Let:
- `n` = number of objects  
- `m` = number of bins  

- **Smallest Fit / Largest Fit Heuristic Loop**

  For each object:
  - Searching for a suitable bin in the AVL tree: `O(log m)`
  - Updating the AVL tree after placing the object (remove and reinsert bin): `O(log m)`

Overall time complexity:

```text
O(n log m)

## Edge Cases Considered

- **Object Too Large**
  - If an object cannot fit into any available bin, a custom exception (e.g., `BinCapacityExceededException`) is raised, as defined in the repository.

- **Duplicate Packing**
  - Attempting to pack the same object more than once triggers a handled error through custom exception handling.

- **Empty Input**
  - Cases with no bins or no objects are handled without crashing, based on defensive checks and exception usage in the code.
