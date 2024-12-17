#include <iostream>
#include <vector>
#include <stack>
#include <set>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace std::chrono;

struct PuzzleState {
    vector<vector<int> > board;
    pair<int, int> blankPos;
    int closeness;

    bool operator<(const PuzzleState& other) const {
        return board < other.board;
    }
};

int manhattanDistance(const vector<vector<int> >& board) {
    int distance = 0;
    int goal[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] != 0) {
                int value = board[i][j];
                int goalRow = (value - 1) / 3;
                int goalCol = (value - 1) % 3;
                distance += abs(i - goalRow) + abs(j - goalCol);
            }
        }
    }
    return distance;
}

vector<PuzzleState> generateMoves(const PuzzleState& state) {
    vector<PuzzleState> moves;
    int row = state.blankPos.first;
    int col = state.blankPos.second;
    vector<pair<int, int> > directions = {make_pair(-1, 0), make_pair(1, 0), make_pair(0, -1), make_pair(0, 1)};

    for (const auto& dir : directions) {
        int newRow = row + dir.first;
        int newCol = col + dir.second;
        if (newRow >= 0 && newRow < 3 && newCol >= 0 && newCol < 3) {
            PuzzleState newState = state;
            swap(newState.board[row][col], newState.board[newRow][newCol]);
            newState.blankPos = make_pair(newRow, newCol);
            newState.closeness = manhattanDistance(newState.board);
            moves.push_back(newState);
        }
    }
    return moves;
}

bool isGoalState(const vector<vector<int> >& board) {
    int goal[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] != goal[i][j]) {
                return false;
            }
        }
    }
    return true;
}

void printBoard(const vector<vector<int> >& board) {
    for (const auto& row : board) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void solve8Puzzle(const vector<vector<int> >& initialBoard) {
    stack<PuzzleState> dfsStack;
    set<vector<vector<int> > > visited;
    vector<vector<vector<int> > > solutionSteps;

    int initialCloseness = manhattanDistance(initialBoard);
    pair<int, int> blankPos;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (initialBoard[i][j] == 0) {
                blankPos = make_pair(i, j);
                break;
            }
        }
    }

    PuzzleState initialState = {initialBoard, blankPos, initialCloseness};
    dfsStack.push(initialState);
    visited.insert(initialBoard);

    auto startTime = high_resolution_clock::now();

    while (!dfsStack.empty()) {
        PuzzleState currentState = dfsStack.top();
        dfsStack.pop();

        solutionSteps.push_back(currentState.board);

        if (isGoalState(currentState.board)) {
            auto endTime = high_resolution_clock::now();
            chrono::duration<double> elapsed = endTime - startTime;

            cout << "Initial Puzzle:" << endl;
            printBoard(initialBoard);

            cout << "Solution Found:" << endl;
            for (const auto& step : solutionSteps) {
                printBoard(step);
            }

            cout << "Solved Puzzle:" << endl;
            printBoard(currentState.board);

            cout << "Time taken: " << elapsed.count() << " seconds" << endl;
            return;
        }

        vector<PuzzleState> nextStates = generateMoves(currentState);
        for (const auto& nextState : nextStates) {
            if (visited.find(nextState.board) == visited.end()) {
                dfsStack.push(nextState);
                visited.insert(nextState.board);
            }
        }
    }

    cout << "No solution exists for the given puzzle." << endl;
}

int main() {
    vector<vector<int> > initialBoard = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 0, 8}
    };

    solve8Puzzle(initialBoard);

    return 0;
}