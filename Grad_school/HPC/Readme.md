# CSC523 Exercises Summary

## Chapter 2: Merge Sort
In this chapter, I implemented the Merge Sort algorithm in Python. The implementation includes a function to perform the merge sort and a function to print the sorted array. The merge sort algorithm is a divide-and-conquer algorithm that recursively divides the array into two halves, sorts each half, and then merges the sorted halves.

## Chapter 7: Exercise 2
This exercise involved working with a PDF document. The details of the exercise are contained within the PDF file `Chp 7 - Exercise 2.pdf`.

## Chapter 10: Graph Representation and MPI
### Exercise 1
In this exercise, I created a graph with 8 vertices and set up some edges between them. I used MPI to distribute the vertices and their edges to different processes. Each process prints out the value stored in its vertex and the edges connected to it.

### Exercise 2
In this exercise, I extended the graph representation to include weights for each edge. I also added a flag to indicate if a vertex is in a specific set (V-VT) and initialized values for each vertex. The program uses MPI to distribute the graph data and compute the minimum edge weight among the vertices in V-VT.

## Chapter 11: Search Algorithms
### Exercise 1: Serial Binary Search
In this exercise, I implemented a serial binary search algorithm in C++. The program creates a sorted list of 2^20 items and searches for 2000 random items in the list. The time taken to complete the search is measured and printed.

### Exercise 2: Parallel 8-Puzzle Solver
In this exercise, I implemented a parallel solver for the 8-puzzle problem using depth-first search (DFS) and MPI. The program generates possible moves, checks for the goal state, and prints the solution steps along with the time taken to find the solution. The parallel implementation distributes the search space among multiple processes to speed up the search.

