# Bin-Packing System  
## Overview
This project implements a bin-packing system utilizing AVL trees for efficient sorting and searching, combined with smallest fit and largest fit algorithms to determine the optimal placement of objects into bins based on their size and other properties. The system ensures that items are packed into bins either by filling the smallest suitable bin (smallest fit) or by placing them into the largest available bin (largest fit).

## Key Features:
- AVL Tree Implementation: For efficient bin management and quick insertion/search.
- Smallest Fit Algorithm: Finds the smallest bin that can accommodate an object.
- Largest Fit Algorithm: Places objects into the largest available bin.
- Custom Exception Handling: Handles errors specific to bin packing (e.g., object too large for any bin).

## File Structure
### 1. main.py
This is the entry point of the project where the bin-packing operations are controlled. The script takes inputs (objects and bins) and manages the packing process using the algorithms defined.

##### Key components:

- Manages input/output for bin-packing operations.
- Calls necessary functions from the AVL tree and bin system modules.
- Implements the bin-packing logic using the smallest and largest fit strategies.

### 2. gcms.py
This file contains functions related to garbage collection or memory management within the project. It ensures that the system runs efficiently without memory leaks by properly managing object creation and deletion as required.

### 3. bin.py
This module defines the Bin class, which is essential to the bin-packing system. Each bin has attributes such as bin_id, capacity, and a collection of objects it contains.

#### Key features:

- Bin class: Represents a container that can hold multiple objects.
- Methods: Includes methods to add, remove, or check the capacity of the bin.
### 4. objects.py
This file defines two key components:

- Color Enum: Defines object colors (BLUE, YELLOW, RED, and GREEN).
- Object Class: Represents an object with object_id, size, color, and a bin_id (initialized as None).
Objects are packed into bins based on their size using either the smallest fit or largest fit algorithms.

### 5. avl.py
This file implements an AVL Tree, a self-balancing binary search tree used to maintain the bins in a sorted order based on their capacity. AVL trees allow for efficient search, insertion, and deletion of bins, ensuring that the system remains efficient as the number of bins grows.

#### Key methods:

- Insert: Adds a new bin to the tree.
- Delete: Removes a bin from the tree.
- Search: Locates bins with appropriate capacity for an object.
### 6. node.py
This file defines the Node class, which is used in the AVL tree structure. Each node contains information about a bin and links to its child nodes.

####Key attributes:

- Bin: Each node represents a bin.
- Left and Right Children: Pointers to child nodes in the AVL tree.
### 7. exceptions.py
This file defines custom exceptions used throughout the system to handle errors specific to the bin-packing process. For example:

- BinCapacityExceededException: Raised when an object is too large for any available bin.
- ObjectAlreadyPackedException: Raised if an object is being packed more than once.

## Algorithms
### 1. Smallest Fit Algorithm
This algorithm places each object into the smallest bin that has enough capacity to accommodate it. This approach aims to reduce space wastage by utilizing bins as efficiently as possible.

### 2. Largest Fit Algorithm
In contrast, the largest fit algorithm places objects into the largest bin available that can accommodate the object. This can be useful when dealing with bins that have very large capacities, ensuring that they are utilized when smaller bins are insufficient.
## Conclusion
This project implements a bin-packing system using AVL trees for efficient bin management, combined with smallest fit and largest fit algorithms to optimize object placement. It mirrors real-world challenges like warehouse storage optimization, where items of varying sizes must be packed into limited spaces efficiently. The system ensures scalability, error handling, and can be extended with additional constraints, providing a solid foundation for applications like logistics, shipping, and inventory management.
 


