# Bin-Packing System Using AVL Trees
## Overview
This project implements a bin-packing system utilizing AVL trees for efficient sorting and searching, combined with smallest fit and largest fit algorithms to determine the optimal placement of objects into bins based on their size and other properties. The system ensures that items are packed into bins either by filling the smallest suitable bin (smallest fit) or by placing them into the largest available bin (largest fit).

## Key Features:
- ** AVL Tree Implementation: For efficient bin management and quick insertion/search.
- ** Smallest Fit Algorithm: Finds the smallest bin that can accommodate an object.
- ** Largest Fit Algorithm: Places objects into the largest available bin.
- ** Custom Exception Handling: Handles errors specific to bin packing (e.g., object too large for any bin).

## File Structure
### 1. main.py
This is the entry point of the project where the bin-packing operations are controlled. The script takes inputs (objects and bins) and manages the packing process using the algorithms defined.

##### Key components:

- **Manages input/output for bin-packing operations.
- **Calls necessary functions from the AVL tree and bin system modules.
- **Implements the bin-packing logic using the smallest and largest fit strategies.


