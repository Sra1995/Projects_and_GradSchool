/*
Write a MPI program that is able to create a graph and print out all the edges at each vertex.
Unless you want to get into classes and multiple files I recommend using a simple struct to represent each vertex.  
For now just have each vertex store a single integer.
For the edges C++ comes with a vector class: std::vector - cppreference.com
Create a graph with 8 vertices and setup some edges between them (hard coding is fine).
Run it with 8 processors and send each processor the information for one of the vertices and have it print out the value stored and the edges there.

 */

#include <mpi.h>                                                                                        // Include the MPI library
#include <iostream>                                                                                     // Include the iostream library for input and output
#include <vector>                                                                                       // Include the vector library

using namespace std;                                                                                    // Use the standard namespace cause I don't want to type std:: before every cout, cin, vector, etc.

class Vertex {                                                                                          // Define the Vertex class
public:
    int value;                                                                                          // Value of the vertex
    vector<int> edges;                                                                                  // Edges of the vertex

    Vertex(int val) : value(val) {}                                                                     // Constructor to initialize the vertex value
};

class Graph {                                                                                           // Define the Graph class
public:
    vector<Vertex> vertices;                                                                            // Vertices of the graph

    Graph(int n) {                                                                                      // Constructor to initialize the graph with n vertices
        for (int i = 0; i < n; ++i) {                                                                   // Iterate over the number of vertices
            vertices.emplace_back(i);                                                                   // Add a new vertex to the graph
        }
    }

    void add_edge(int u, int v) {                                                                       // Function to add an edge between two vertices
        vertices[u].edges.push_back(v);                                                                 // Add edge from vertex u to vertex v
    }

    const Vertex& get_vertex(int i) const {                                                             // Function to get a vertex by index
        return vertices[i];                                                                             // Return the vertex at index i
    }

    void print_graph() const {                                                                          // Function to print the graph
        cout << "Adjacency List for the Graph: " << endl;                                               // Print the header
        for (const auto& vertex : vertices) {                                                           // Iterate over each vertex
            cout << "Vertex " << vertex.value << ": ";                                                  // Print the vertex value
            for (int edge : vertex.edges) {                                                             // Iterate over each edge of the vertex
                cout << edge << " ";                                                                    // Print the edge
            }
            cout << endl;                                                                               // Print a new line
        }
    }
};

int main()                                                                                              // Main function
{
    MPI_Init(NULL, NULL);                                                                               // Initialize the MPI environment

    int world_rank;                                                                                     // Variable to store the rank of the process
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);                                                         // Get the rank of the process

    int world_size;                                                                                     // Variable to store the number of processes
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);                                                         // Get the number of processes

    int n = 8;                                                                                          // Number of vertices
    Graph g(n);                                                                                         // Create a graph with 8 vertices

    if (world_rank == 0) {                                                                              // Only the root process initializes the graph
        g.add_edge(0, 1);                                                                               // Add edge between vertex 0 and 1
        g.add_edge(0, 2);                                                                               // Add edge between vertex 0 and 2
        g.add_edge(0, 3);                                                                               // Add edge between vertex 0 and 3
        g.add_edge(1, 4);                                                                               // Add edge between vertex 1 and 4
        g.add_edge(1, 5);                                                                               // Add edge between vertex 1 and 5
        g.add_edge(2, 6);                                                                               // Add edge between vertex 2 and 6
        g.add_edge(2, 7);                                                                               // Add edge between vertex 2 and 7

        for (int i = 1; i < world_size; ++i) {                                                          // Send vertex information to each process
            int num_edges = g.get_vertex(i).edges.size();                                               // Get the number of edges for the vertex
            MPI_Send(&num_edges, 1, MPI_INT, i, 0, MPI_COMM_WORLD);                                     // Send the number of edges to the process
            MPI_Send(g.get_vertex(i).edges.data(), num_edges, MPI_INT, i, 0, MPI_COMM_WORLD);           // Send the edges to the process
        }
    } else {                                                                                            // Other processes receive the vertex information
        int num_edges;                                                                                  // Variable to store the number of edges
        MPI_Recv(&num_edges, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);                      // Receive the number of edges from the root process
        g.vertices[world_rank].edges.resize(num_edges);                                                 // Resize the edges vector to hold the edges
        MPI_Recv(g.vertices[world_rank].edges.data(), num_edges, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE); // Receive the edges from the root process
    }

    // Each process prints its vertex and edges
    if (world_rank < n) {                                                                               // Check if the process rank is less than the number of vertices
        const Vertex& v = g.get_vertex(world_rank);                                                     // Get the vertex for the process rank
        cout << "Process " << world_rank << " has vertex " << v.value << " with edges: ";               // Print the vertex value
        for (int edge : v.edges) {                                                                      // Iterate over each edge of the vertex
            cout << edge << " ";                                                                        // Print the edge
        }
        cout << endl;                                                                                   // Print a new line
    }

    MPI_Finalize();                                                                                     // Finalize the MPI environment
    return 0;                                                                                           // Indicate successful execution
}
