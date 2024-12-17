# Algorithm Steps for Solving the 8-Puzzle using a Parallel Approach

## Problem Setup
1. Represent the 8-puzzle as a 3x3 grid where:
   - Each number represents a tile.
   - `0` represents the blank tile.
2. The goal state is the grid with numbers arranged sequentially in row-major order, with the blank tile at the last position.

## Parallel Algorithm

### Step 1: Initialize the Puzzle State
1. Define the starting state of the puzzle as a 2D array.
2. Identify the position of the blank tile (row and column indices).
3. Compute the initial closeness measure using the Manhattan Distance:
   - For each tile, calculate the distance between its current position and its target position in the goal state.

### Step 2: Define Supporting Structures
1. Use a priority queue to manage states for exploration, sorted by their closeness measure.
2. Maintain a shared set of visited states (accessible by all processors) to avoid revisiting states.
3. Use a stack or queue local to each processor to explore assigned paths.
4. Prepare a mechanism to pass information between processors about completed or promising paths.

### Step 3: Distribute Initial Paths Across Processors
1. Generate all possible moves from the starting state:
   - Each move corresponds to swapping the blank tile with an adjacent tile.
   - Compute the closeness measure for each resulting state.
2. Distribute these initial states among available processors:
   - Assign one or more states to each processor based on availability.
   - Ensure load balancing by evenly dividing the initial states.

### Step 4: Parallel Exploration
1. Each processor independently explores its assigned paths using Depth-First Search (DFS):
   - For each state, generate all possible next moves.
   - Compute the closeness measure for each move.
   - Add unexplored states to the local stack or queue.
   - Mark visited states in the shared set to avoid revisiting.
2. If a processor finds a goal state:
   - Broadcast the success to all other processors.
   - Terminate the search on all processors.
3. If a processor exhausts its paths without success:
   - Request additional states from the shared priority queue or other processors.

### Step 5: Communication Between Processors
1. Use MPI for inter-processor communication to:
   - Share promising paths or states between processors.
   - Broadcast success or termination signals.
   - Synchronize access to the shared visited set to prevent race conditions.
2. If the priority queue contains promising paths:
   - Assign new paths dynamically to processors with idle capacity.

### Step 6: Handle Path Abandonment and Path Selection
1. Evaluate the closeness measure at each step:
   - Focus on paths where the closeness measure improves significantly.
   - Abandon paths with minimal improvement or where no progress is made after several moves.
2. Track paths explored by each processor:
   - Maintain a local list of tried paths for efficient backtracking.
   - Share this information periodically with the shared visited set.

### Step 7: Termination
1. The algorithm terminates when:
   - A processor finds the goal state and broadcasts success.
   - All processors exhaust their assigned and shared paths without finding a solution.
2. If no solution is found, print "No solution exists for the given puzzle." and terminate.

## Reasoning Behind Path Assignment
1. Assign paths based on initial closeness measure:
   - States with lower closeness measures are prioritized for exploration.
2. Ensure diversity in paths assigned to processors:
   - Distribute states with varying closeness measures to prevent all processors exploring similar paths.
3. Dynamically reassign paths to idle processors to maximize utilization.

## Testing
1. Validate the algorithm with solvable initial states.
2. Test for unsolvable states to ensure proper termination.
3. Use edge cases like already solved puzzles or maximum-depth configurations.
4. Verify load balancing and communication efficiency between processors.
5. Confirm correctness of the solution by ensuring the goal state is reached and validated.

### Example Output
```plaintext
Rank 2 waiting to receive state.
Rank 5 waiting to receive state.
Rank 7 waiting to receive state.
Rank 3 waiting to receive state.
Rank 6 waiting to receive state.
Rank 4 waiting to receive state.
Rank 1 waiting to receive state.
Initial State:
1 2 3 
4 5 6 
7 8 0 
Rank 0 sending state to rank 1
Rank 0 sending state to rank 2
Rank 0 sending state to rank 3
Rank 0 sending state to rank 4
Rank 0 sending state to rank 5
Rank 0 sending state to rank 6
Rank 4 received state.
Rank 4 found goal state.
Rank 4 sending termination signal.
Rank 2 received state.
Rank 2 found goal state.
Rank 2 sending termination signal.
Rank 0 sending state to rank 7
Rank 0 received move from rank 4
Goal state found by rank 4
1 2 3 
4 5 6 
7 8 0 
Solution found:
1 2 3 
4 5 6 
7 8 0 
Rank 5 sending termination signal.
Rank 6 received state.
Rank 6 found goal state.
Rank 6 sending termination signal.
Time taken: 0.004087 seconds
```
