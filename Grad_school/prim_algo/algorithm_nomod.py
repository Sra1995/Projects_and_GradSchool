import random                                                                   # Import the random module for generating random numbers
import time                                                                     # Import the time module for measuring execution time

class Node:
    def __init__(self, key):                                                    # Constructor method for initializing a node with a key
        self.key = key                                                          # Initialize the key attribute of the node with the provided key
        self.left = None                                                        # Initialize the left child pointer to None
        self.right = None                                                       # Initialize the right child pointer to None


class Edge:
    def __init__(self, source, target, weight):                                 # Constructor method for initializing an edge with source, target, and weight
        self.source = source                                                    # Initialize the source attribute of the edge
        self.target = target                                                    # Initialize the target attribute of the edge
        self.weight = weight                                                    # Initialize the weight attribute of the edge

class BinarySearchTree:
    def __init__(self):                                                         # Constructor method for initializing a Binary Search Tree
        self.root = None                                                        # Initialize the root attribute to None

    def insert(self, key):                                                      # Method for inserting a key into the binary search tree
        self.root = self._insert(self.root, key)                                # Update the root after inserting the key

    def _insert(self, root, key):                                               # Helper method for recursive insertion
        if root is None:                                                        # If the current root is None, create a new node with the key
            return Node(key)

        if key < root.key:                                                      # If the key is less than the current root's key, recursively insert on the left
            root.left = self._insert(root.left, key)
        elif key > root.key:                                                    # If the key is greater than the current root's key, recursively insert on the right
            root.right = self._insert(root.right, key)

        return root                                                             # Return the updated root

    def inorder_traversal(self, root):                                          # Method for performing an inorder traversal of the binary search tree
        result = []                                                             # Initialize an empty list to store traversal results
        if root:                                                                # If the root is not None
            result = self.inorder_traversal(root.left)                          # Recursively traverse the left subtree
            result.append(root.key)                                             # Append the current root's key to the result list
            result += self.inorder_traversal(root.right)                        # Recursively traverse the right subtree
        return result                                                           # Return the traversal result

    def add_random_connections(self, edges, graph, root):                       # Method for adding random connections to the graph based on the binary search tree
        if root:                                                                # If the current root is not None
            self.add_random_connections(edges, graph, root.left)                # Recursively add connections in the left subtree
            self.add_random_connections(edges, graph, root.right)               # Recursively add connections in the right subtree

            if random.random() < 0.2:                                           # Generate a random number to determine if a connection should be added
                target_key = random.choice(self.inorder_traversal(self.root))   # Randomly select a node in the tree to connect to
                edges.append(Edge(root.key, target_key, random.uniform(0, 1)))  # Assuming random weights

    def mst_prim_custom(self, edges, graph):                                    # Custom implementation of Prim's algorithm
        start_time = time.time()                                                # Record the start time of the algorithm

        visited = set()                                                         # Initialize a set to track visited nodes
        edges.sort(key=lambda edge: edge.weight)                                # Sort edges based on weights
        
        mst = []                                                                # Initialize the Minimum Spanning Tree (MST)

        for edge in edges:                                                      # Iterate through sorted edges
            if edge.source not in visited or edge.target not in visited:        # Check if the edge connects unvisited nodes
                mst.append(edge)                                                # Add the edge to the MST
                visited.add(edge.source)                                        # Mark the source node as visited
                visited.add(edge.target)                                        # Mark the target node as visited

        end_time = time.time()                                                  # Record the end time of the algorithm
        execution_time = end_time - start_time                                  # Calculate the execution time

        print(f"Sample Execution Time: {execution_time:.6f} seconds")           # Output execution time for each sample
                                                                                #disable these print functinos except print() if you wish to only see execution time
        print("Graph for Sample:")                                              # Print the nodes and edges of the graph
        print("Nodes:", sorted(list(visited)))                                  # Sorted for consistency
        print("Edges:", [(edge.source, edge.target) for edge in mst])
        print()

        return mst, execution_time                                              # Return the MST and execution time

                                                                                # Function to run the process for a given size and number of samples
def run_samples(size, num_samples):
    total_execution_time = 0                                                    # Initialize the total execution time

    for sample in range(1, num_samples + 1):                                    # Iterate through the specified number of samples
        bst = BinarySearchTree()                                                # Create a binary search tree

        unique_values = random.sample(range(1, size + 1), size)                 # Generate unique random integers based on the size

        for value in unique_values:                                             # Insert unique values into the binary search tree
            bst.insert(value)

        edges = []                                                              # Initialize edges list

        bst.add_random_connections(edges, None, bst.root)                       # Create a graph and add random connections

        _, execution_time = bst.mst_prim_custom(edges, None)                    # Perform MST-Prim algorithm and measure execution time

        total_execution_time += execution_time                                  # Accumulate the total execution time

    average_execution_time = total_execution_time / num_samples                 # Calculate the average execution time
    print(f"Size: {size}, Average Execution Time: {average_execution_time:.6f} seconds")  # Output average execution time

# Run 20 samples for each size (100, 400, 1600)
run_samples(100, 20)
run_samples(400, 20)
run_samples(1600, 20)
