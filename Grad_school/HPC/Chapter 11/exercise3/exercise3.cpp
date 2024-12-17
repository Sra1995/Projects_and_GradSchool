// Algorithm Steps for Solving the 8-Puzzle using a Parallel Approach

#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <mpi.h>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace std::chrono;

const int N = 3; // Define the 8-puzzle grid size

// Global variables
bool goalFound = false;
vector<vector<int>> goalStateFound;
set<vector<vector<int>>> visited;

// Function to calculate the Manhattan Distance
int manhattanDistance(const vector<vector<int>>& state, const vector<vector<int>>& goal) {
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
void printState(const vector<vector<int>>& state) {
    for (const auto& row : state) {
        for (const auto& tile : row) {
            cout << tile << " ";
        }
        cout << endl;
    }
}

// Function to check if the current state is the goal state
bool isGoalState(const vector<vector<int>>& state, const vector<vector<int>>& goal) {
    return state == goal;
}

// Function to find the position of the empty tile (0)
pair<int, int> findEmptyTile(const vector<vector<int>>& state) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (state[i][j] == 0) {
                return {i, j};
            }
        }
    }
    return {-1, -1}; // Should never reach here if the state is valid
}

// Function to generate possible moves from the current state
vector<vector<vector<int>>> generateMoves(const vector<vector<int>>& state, int x, int y) {
    vector<vector<vector<int>>> moves;
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (const auto& dir : directions) {
        int newX = x + dir.first;
        int newY = y + dir.second;
        if (newX >= 0 && newX < N && newY >= 0 && newY < N) {
            vector<vector<int>> newState = state;
            swap(newState[x][y], newState[newX][newY]);
            moves.push_back(newState);
        }
    }
    return moves;
}

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    auto start = high_resolution_clock::now();

    vector<vector<int>> initialState = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 0}
    };

    vector<vector<int>> goalState = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 0}
    };

    if (rank == 0) {
        // Master process
        cout << "Initial State:" << endl;
        printState(initialState);

        vector<int> flatState(N * N);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                flatState[i * N + j] = initialState[i][j];
            }
        }

        for (int i = 1; i < size; ++i) {
            std::cout << "Rank 0 sending state to rank " << i << std::endl;
            MPI_Send(flatState.data(), N * N, MPI_INT, i, 0, MPI_COMM_WORLD);
        }

        int terminationCount = 0;
        while (terminationCount < size - 1) {
            MPI_Status status;
            MPI_Probe(MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

            if (status.MPI_TAG == 1) {
                vector<int> move(N * N);
                MPI_Recv(move.data(), N * N, MPI_INT, status.MPI_SOURCE, 1, MPI_COMM_WORLD, &status);
                std::cout << "Rank 0 received move from rank " << status.MPI_SOURCE << std::endl;
                // Process the move (add your logic here)
                vector<vector<int>> newState(N, vector<int>(N));
                for (int i = 0; i < N; ++i) {
                    for (int j = 0; j < N; ++j) {
                        newState[i][j] = move[i * N + j];
                    }
                }
                if (visited.find(newState) == visited.end()) {
                    visited.insert(newState);
                    if (isGoalState(newState, goalState)) {
                        goalFound = true;
                        goalStateFound = newState;
                        std::cout << "Goal state found by rank " << status.MPI_SOURCE << std::endl;
                        printState(goalStateFound);
                        break;
                    } else {
                        // Assign new paths to explore
                        pair<int, int> blankPos = findEmptyTile(newState);
                        auto newMoves = generateMoves(newState, blankPos.first, blankPos.second);
                        for (const auto& newMove : newMoves) {
                            vector<int> flatNewMove(N * N);
                            for (int i = 0; i < N; ++i) {
                                for (int j = 0; j < N; ++j) {
                                    flatNewMove[i * N + j] = newMove[i][j];
                                }
                            }
                            MPI_Send(flatNewMove.data(), N * N, MPI_INT, status.MPI_SOURCE, 1, MPI_COMM_WORLD);
                        }
                    }
                }
            } else if (status.MPI_TAG == 2) {
                MPI_Recv(nullptr, 0, MPI_INT, status.MPI_SOURCE, 2, MPI_COMM_WORLD, &status);
                std::cout << "Rank 0 received termination signal from rank " << status.MPI_SOURCE << std::endl;
                terminationCount++;
            }
        }

        if (goalFound) {
            std::cout << "Solution found:" << std::endl;
            printState(goalStateFound);
        } else {
            std::cout << "No solution found." << std::endl;
        }
    } else {
        // Worker processes
        vector<int> receivedState(N * N);

        MPI_Status status;
        std::cout << "Rank " << rank << " waiting to receive state." << std::endl;
        MPI_Recv(receivedState.data(), N * N, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
        std::cout << "Rank " << rank << " received state." << std::endl;

        vector<vector<int>> state(N, vector<int>(N));
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                state[i][j] = receivedState[i * N + j];
            }
        }

        if (isGoalState(state, goalState)) {
            goalFound = true;
            goalStateFound = state;
            std::cout << "Rank " << rank << " found goal state." << std::endl;
            // Send the goal state to the master process
            vector<int> flatGoalState(N * N);
            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < N; ++j) {
                    flatGoalState[i * N + j] = state[i][j];
                }
            }
            MPI_Send(flatGoalState.data(), N * N, MPI_INT, 0, 1, MPI_COMM_WORLD);
        } else {
            pair<int, int> blankPos = findEmptyTile(state);
            auto moves = generateMoves(state, blankPos.first, blankPos.second);

            for (const auto& move : moves) {
                if (visited.find(move) == visited.end() && !goalFound) {
                    visited.insert(move);
                    std::cout << "Rank " << rank << " sending move." << std::endl;
                    vector<int> flatMove(N * N);
                    for (int i = 0; i < N; ++i) {
                        for (int j = 0; j < N; ++j) {
                            flatMove[i * N + j] = move[i][j];
                        }
                    }
                    MPI_Send(flatMove.data(), N * N, MPI_INT, 0, 1, MPI_COMM_WORLD);
                }
            }
        }

        std::cout << "Rank " << rank << " sending termination signal." << std::endl;
        MPI_Send(nullptr, 0, MPI_INT, 0, 2, MPI_COMM_WORLD);
    }

    MPI_Finalize();

    auto end = high_resolution_clock::now();
    duration<double> duration = end - start;
    double time_taken = duration.count();

    if (rank == 0) {
        std::cout << "Time taken: " << fixed << time_taken << " seconds" << std::endl;
    }

    return 0;
}