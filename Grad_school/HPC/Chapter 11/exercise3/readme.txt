Algorithm Steps for Solving the 8-Puzzle using a Parallel Approach

Problem Setup:
1. Imagine the 8-puzzle as a 3x3 grid where each number is a tile, and `0` is the blank tile.
2. The goal is to arrange the numbers sequentially in row-major order, with the blank tile at the last position.

Parallel Algorithm:

Step 1: Initialize the Puzzle State
1. Start by defining the puzzle's initial state as a 2D array.
2. Find the blank tile's position (row and column).
3. Calculate the initial closeness measure using the Manhattan Distance for each tile.

Step 2: Define Supporting Structures
1. Use a priority queue to manage states for exploration, sorted by their closeness measure.
2. Keep a shared set of visited states to avoid revisiting.
3. Each processor should have a local stack or queue to explore assigned paths.
4. Set up a way to share information between processors about completed or promising paths.

Step 3: Distribute Initial Paths Across Processors
1. Generate all possible moves from the starting state by swapping the blank tile with an adjacent tile and compute the closeness measure for each resulting state.
2. Distribute these initial states among processors, ensuring load balancing.

Step 4: Parallel Exploration
1. Each processor explores its assigned paths using Depth-First Search (DFS):
    - Generate all possible next moves for each state.
    - Compute the closeness measure for each move.
    - Add unexplored states to the local stack or queue.
    - Mark visited states in the shared set.
2. If a processor finds the goal state, it broadcasts the success and all processors terminate the search.
3. If a processor runs out of paths, it requests additional states from the shared priority queue or other processors.

Step 5: Communication Between Processors
1. Use MPI for inter-processor communication to:
    - Share promising paths or states.
    - Broadcast success or termination signals.
    - Synchronize access to the shared visited set.
2. Assign new paths dynamically to idle processors if the priority queue has promising paths.

Step 6: Handle Path Abandonment and Path Selection
1. Evaluate the closeness measure at each step and focus on paths with significant improvement.
2. Track paths explored by each processor and share this information periodically.

Step 7: Termination
1. The algorithm terminates when a processor finds the goal state and broadcasts success, or all processors exhaust their paths without finding a solution.
2. If no solution is found, print "No solution exists for the given puzzle." and terminate.

Reasoning Behind Path Assignment:
1. Assign paths based on the initial closeness measure, prioritizing states with lower measures.
2. Ensure diversity in paths assigned to processors to prevent similar paths exploration.
3. Dynamically reassign paths to idle processors to maximize utilization.

Testing:
1. Validate the algorithm with solvable initial states.
2. Test for unsolvable states to ensure proper termination.
3. Use edge cases like already solved puzzles or maximum-depth configurations.
4. Verify load balancing and communication efficiency.
5. Confirm correctness by ensuring the goal state is reached and validated.

Example Output:

can be found in the `rawoutput_mpi.txt` file.

