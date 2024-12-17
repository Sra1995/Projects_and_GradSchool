# 8-Puzzle Solver

This project implements a parallel approach to solve the 8-puzzle problem using MPI (Message Passing Interface). The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one blank space. The goal is to rearrange the tiles to match a specified goal state.

## Features

- **Parallel Processing**: Utilizes MPI to distribute the computation across multiple processes.
- **Manhattan Distance**: Uses the Manhattan Distance heuristic to guide the search.
- **Priority Queue**: Manages states for exploration using a priority queue.
- **Path Reconstruction**: Reconstructs and prints the path from the initial state to the goal state.

## Algorithm and Time Complexity

The algorithm leverages the Manhattan Distance heuristic to estimate the cost of reaching the goal state from the current state. This heuristic is particularly effective for the 8-puzzle as it provides a good approximation of the number of moves required. The priority queue ensures that states with lower estimated costs are explored first, which helps in finding the solution efficiently.

In terms of time complexity, the worst-case scenario for the 8-puzzle solver is exponential, as it may need to explore a large number of states. However, the use of parallel processing with MPI significantly reduces the time taken by distributing the workload across multiple processes.

## Findings on MacBook Air M1 (8GB RAM)

Running the 8-puzzle solver on a MacBook Air M1 with 8GB of RAM yielded impressive results. The solver was able to find the solution in a fraction of a second, demonstrating the efficiency of the parallel approach. Here are some sample outputs:

```
Initial puzzle state:
1 2 3 
4 0 5 
6 7 8 
Goal state found!
Solution steps:
1 2 3 
4 0 5 
6 7 8 

1 2 3 
0 4 5 
6 7 8 

...

Time taken to solve: 0.00363133 seconds
```

### Comparison

- **Serial Solver (exercise2.cpp)**: The serial solver consistently solved the puzzle in a fraction of a second, with times ranging from approximately 6.8875e-05 to 0.00011475 seconds.
- **Parallel Solver (exercise3.cpp)**: The parallel solver also solved the puzzle efficiently, with times ranging from approximately 0.00331442 to 0.00419883 seconds. The parallel approach is particularly beneficial for larger and more complex puzzles, where the workload can be distributed across multiple processes.

The parallel implementation demonstrates the potential for significant performance improvements, especially as the complexity of the puzzle increases.

## Additional Information

- **Created by**: Sajjad Al Saffar
- **Course**: CSC523 - Advanced Parallel Computing
- **Institution**: Shippensburg University, Fall 2024

