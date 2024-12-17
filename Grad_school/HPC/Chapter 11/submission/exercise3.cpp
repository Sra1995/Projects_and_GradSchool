// Algorithm Steps for Solving the 8-Puzzle using a Parallel Approach

#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <mpi.h>
#include <chrono>
#include <map>

using namespace std;

// Define the 8-puzzle grid size
const int N = 3;

// Function to calculate the Manhattan Distance
int manhattanDistance(const vector<vector<int> >& state, const vector<vector<int> >& goal) {
    int distance = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (state[i][j] != 0) {
                for (int x = 0; x < N; ++x) {
                    for (int y = 0; y < N; ++y) {
                        if (state[i][j] == goal[x][y]) {
                            distance += abs(i - x) + abs(j - y);
                        }
                    }
                }
            }
        }
    }
    return distance;
}

// Function to print the puzzle state
void printState(const vector<vector<int> >& state) {
    for (const auto& row : state) {
        for (int tile : row) {
            cout << tile << " ";
        }
        cout << endl;
    }
}

// Function to check if the current state is the goal state
bool isGoalState(const vector<vector<int> >& state, const vector<vector<int> >& goal) {
    return state == goal;
}

// Function to generate possible moves from the current state
vector<vector<vector<int> > > generateMoves(const vector<vector<int> >& state, int blankRow, int blankCol) {
    vector<vector<vector<int> > > moves;
    vector<pair<int, int> > directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (const auto& dir : directions) {
        int newRow = blankRow + dir.first;
        int newCol = blankCol + dir.second;
        if (newRow >= 0 && newRow < N && newCol >= 0 && newCol < N) {
            vector<vector<int> > newState = state;
            swap(newState[blankRow][blankCol], newState[newRow][newCol]);
            moves.push_back(newState);
        }
    }
    return moves;
}

// Function to find the position of the blank tile
pair<int, int> findBlankTile(const vector<vector<int> >& state) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (state[i][j] == 0) {
                return {i, j};
            }
        }
    }
    return {-1, -1}; // Should never reach here if the state is valid
}

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Define the starting state and goal state
    vector<vector<int> > startState = {{1, 2, 3}, {4, 0, 5}, {6, 7, 8}};
    vector<vector<int> > goalState = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};

    if (rank == 0) {
        cout << "Initial puzzle state:" << endl;
        printState(startState);
    }

    // Identify the position of the blank tile in the start state
    pair<int, int> blankPos = findBlankTile(startState);

    // Compute the initial closeness measure using the Manhattan Distance
    int initialDistance = manhattanDistance(startState, goalState);

    // Priority queue to manage states for exploration
    priority_queue<pair<int, vector<vector<int> > >, vector<pair<int, vector<vector<int> > > >, greater<pair<int, vector<vector<int> > > > > pq;
    pq.push({initialDistance, startState});

    // Shared set of visited states
    set<vector<vector<int> > > visited;
    visited.insert(startState);

    // Map to store the parent of each state
    map<vector<vector<int> >, vector<vector<int> > > parent;
    parent[startState] = {};

    // Start timing
    auto startTime = chrono::high_resolution_clock::now();

    // Main parallel exploration loop
    bool goalFound = false;
    vector<vector<int> > currentState; // Declare currentState here
    while (!pq.empty() && !goalFound) {
        currentState = pq.top().second;
        pq.pop();

        if (isGoalState(currentState, goalState)) {
            goalFound = true;
            if (rank == 0) {
                cout << "Goal state found!" << endl;
            }
            break;
        }

        // Find the position of the blank tile in the current state
        blankPos = findBlankTile(currentState);

        // Generate possible moves from the current state
        vector<vector<vector<int> > > moves = generateMoves(currentState, blankPos.first, blankPos.second);
        for (const auto& move : moves) {
            if (visited.find(move) == visited.end()) {
                int distance = manhattanDistance(move, goalState);
                pq.push({distance, move});
                visited.insert(move);
                parent[move] = currentState; // Store the parent state
            }
        }
    }

    // Check if any process found the goal state
    int globalGoalFound;
    MPI_Allreduce(&goalFound, &globalGoalFound, 1, MPI_INT, MPI_LOR, MPI_COMM_WORLD);

    if (globalGoalFound && rank == 0) {
        auto endTime = chrono::high_resolution_clock::now();
        chrono::duration<double> elapsed = endTime - startTime;

        // Reconstruct the path from the initial state to the goal state
        vector<vector<vector<int> > > path;
        for (vector<vector<int> > state = currentState; !state.empty(); state = parent[state]) {
            path.push_back(state);
        }
        reverse(path.begin(), path.end());

        // Print each step of the solution
        cout << "Solution steps:" << endl;
        for (const auto& step : path) {
            printState(step);
            cout << endl;
        }

        cout << "Time taken to solve: " << elapsed.count() << " seconds" << endl;
    } else if (!globalGoalFound && rank == 0) {
        cout << "No solution exists for the given puzzle." << endl;
    }

    MPI_Finalize();
    return 0;
}