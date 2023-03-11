from graph import Graph
from graph import Node


g = Graph()
g.add_node(5)
g.add_node(7)

# Test graph with only nodes
print("Test 1:")
g.print_graph()

# Test graph with two nodes, and connect one to a node that doesn't exist
print("Test 2:")
g.add_edge(5, 9)
g.print_graph()

# Add edge between two nodes that already exist
print("Test 3:")
g.add_node(1)
g.add_edge(1,5)
g.print_graph()

# Add edge between two nodes that already have one
print("Test 4:")
g.add_edge(5, 1)
g.print_graph()

# Clear test
g.clear()
print("Clear test:")
g.print_graph()

# Test adding nodes from list
g.add_nodes([1,2,3,4,5,6,7,8])
print("Nodes from list test:")
g.print_graph()

# Test adding edges from list
g.add_edges([(1,7),(7,2),(7,4),(7,8),(8,5),(5,3),(5,6)])
print("Edges from list test:")
g.print_graph()

# Add BFS/DFS test data


# BFS test
bfs_trav = g.bfs_traversal(5)
print("BFS Traversal:")
print(bfs_trav)

# DFS test
dfs_trav = g.dfs_traversal(5)
print("DFS Traversal:")
print(dfs_trav)

# Path u-w
path = g.path(5, 7)
print("Path from 5 to 7 is:")
print(path)

# Path u-w
path = g.path(6, 7)
print("Path from 6 to 7 is:")
print(path)

# Path u-w
path = g.path(3, 7)
print("Path from 3 to 7 is:")
print(path)

# Path u-w
path = g.path(3, 4)
print("Path from 3 to 4 is:")
print(path)

# Shortest paths
shortest_paths = g.shortest_paths(3)
print("Shortest paths from 3 to the rest of the nodes are:")
print(shortest_paths)