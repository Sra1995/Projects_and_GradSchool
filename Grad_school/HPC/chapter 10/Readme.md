MPI Program to Represent a Graph and Print All Edges at Each Vertex

Objective

The goal of this assignment is to create a parallel program using MPI that represents a graph with 8 vertices and prints out all the edges for each vertex. The program is expected to distribute the information of the graph across 8 processors, where each processor prints the information of one vertex and its corresponding edges.

Approach

	1.	Graph Representation:
	•	We represent the graph using a class Graph and a struct Vertex.
	•	Each Vertex contains:
	•	An integer value (value), which represents the vertex itself.
	•	A vector of integers (edges), which stores the list of vertices connected to the current vertex.
	•	We use a simple undirected graph with hardcoded edges between vertices.
	2.	Graph Creation:
	•	The graph is initialized with 8 vertices.
	•	Edges are added between certain vertices to form a sample graph.
	3.	Parallelization with MPI:
	•	We initialize MPI with MPI_Init.
	•	The rank of each process is retrieved using MPI_Comm_rank, which allows us to assign a specific vertex to each processor.
	•	Each processor prints the value and edges of its assigned vertex.
	•	MPI is finalized using MPI_Finalize.
	4.	Graph Edges:
	•	The edges are hardcoded for simplicity. Each vertex has a set of edges connecting it to other vertices.
	5.	Expected Output:
	•	The output is the adjacency list of the graph where each process prints the vertex and its connected edges.

Explanation of the Code

	•	Graph Representation:
	•	A graph is represented by a Graph class, which contains a vector of Vertex structs. Each Vertex stores its value (an integer) and a list of connected vertices (edges).
	•	Edge Addition:
	•	The function add_edge is used to create an undirected edge between two vertices u and v by adding each vertex to the other’s edge list.
	•	MPI Parallelization:
	•	MPI initializes using MPI_Init and finalizes with MPI_Finalize.
	•	The process rank (world_rank) determines which vertex each process is responsible for.
	•	Each process prints its assigned vertex and its connected edges.
	•	Edge Display:
	•	Each MPI process will display its vertex’s value and the list of edges that connect to it. The output order may vary depending on the execution order of processes.

Sample Output

When running the program with 8 processes (one for each vertex), the output may look like this:

mpirun -np 3 ./exercise1                    
Process 0 has vertex 0 with edges: 1 2 3 
Process 1 has vertex 1 with edges: 4 5 
Process 2 has vertex 2 with edges: 6 7 

mpirun -np 4 ./exercise1                    
Process 0 has vertex 0 with edges: 1 2 3 
Process 1 has vertex 1 with edges: 4 5 
Process 2 has vertex 2 with edges: 6 7 
Process 3 has vertex 3 with edges: 

mpirun -np 8 ./exercise1                    
Process 0 has vertex 0 with edges: 1 2 3 
Process 2 has vertex 2 with edges: 6 7 
Process 4 has vertex 4 with edges: 
Process 7 has vertex 7 with edges: 
Process 6 has vertex 6 with edges: 
Process 5 has vertex 5 with edges: 
Process 3 has vertex 3 with edges: 
Process 1 has vertex 1 with edges: 4 5 

Each process prints the information for one vertex and its connected edges. The order of the processes may differ between runs, but each process correctly outputs the edges for its assigned vertex.

Conclusion

This MPI program effectively demonstrates parallel graph representation and printing the adjacency list of the graph. Each process is assigned a vertex and prints its corresponding edges. The graph structure and parallel execution allow for efficient representation and traversal across multiple processes.

