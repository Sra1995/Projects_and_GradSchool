# Algorithm Steps for Solving the 8-Puzzle using DFS

## Problem Setup
1. Represent the 8-puzzle as a 3x3 grid where:
   - Each number represents a tile.
   - `0` represents the blank tile.
2. The goal state is the grid with numbers arranged sequentially in row-major order, with the blank tile at the last position.

## Algorithm

### Step 1: Initialize the Puzzle State
1. Define the starting state of the puzzle as a 2D array.
2. Identify the position of the blank tile (row and column indices).
3. Compute the initial closeness measure using the Manhattan Distance:
   - For each tile, calculate the distance between its current position and its target position in the goal state.

### Step 2: Define Supporting Structures
1. Use a stack for Depth-First Search (DFS).
2. Maintain a set of visited states to avoid revisiting the same configuration.
3. Define a method to generate all possible moves:
   - The blank tile can move up, down, left, or right, provided the move is within bounds.
   - Swap the blank tile with the adjacent tile in the chosen direction to generate a new state.

### Step 3: Push Initial State into the Stack
1. Push the initial board state, blank tile position, and closeness measure onto the stack.
2. Add the initial state to the visited set.

### Step 4: Perform DFS
1. While the stack is not empty:
   - Pop the top state from the stack.
   - Check if the current state matches the goal state:
     - If yes, print "Solution Found" and terminate the algorithm.
     - If no, proceed to generate possible next states.
2. For each possible next state:
   - Compute its closeness measure.
   - If the state is not in the visited set:
     - Add it to the stack.
     - Mark it as visited.

### Step 5: Handle Backtracking
1. When backtracking occurs (i.e., no moves lead to a solution from a state):
   - Remove the current state from the visited set.
   - Continue exploring other branches of the tree.

### Step 6: Termination
1. If the stack becomes empty and no solution is found:
   - Print "No solution exists for the given puzzle." and terminate.

## Additional Notes
- The Manhattan Distance ensures that the algorithm explores states closer to the goal more effectively.
- The DFS approach may not guarantee the shortest solution path but is computationally efficient for smaller puzzles like the 8-puzzle.
- Loop detection through the visited set prevents infinite cycles and reduces redundant computations.

## Testing
- Validate the algorithm with solvable initial states.
- Ensure it correctly identifies unsolvable states.
- Test edge cases like already solved puzzles or maximum depth configurations.

