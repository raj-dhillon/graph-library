#  Title:		A simple implementation of a graph library for Python using adjacency lists.
# 
#  Features:    This graph library allows a user to develop an undirected and unweighted graph for any given number of
#               nodes and edges. It allows the nodes and edges to be added individually or through a list for fast creation.
#               Some useful methods in this library are: 
#                   The BFS traversal, which returns a list of tuples each demonstrating
#                       the order in which they were found.
# 
#                   The DFS traversal, which is similar to the BFS traversal but does so
#                       using a DFS algorithm.
# 
#                   A path search, which allows the user to find the shortest path between two nodes.
# 
#                   A shortest paths search, which returns the shortest pass from a specific node to every node
#                       in the graph that it is capable of visiting.
# 
#  Author:		Rajdeep Dhillon
#  Date:		March 11, 2023

from collections import deque

class Graph:
    def __init__(self) -> None:
        self.list = dict()

    # Allows you to add a single vertex to the graph
    def add_node(self, node):
        if not self.list.get(node):
            self.list[node] = []
        else:
            print("Node already exists!")

    # Allows you to add multiple vertices to the graph
    def add_nodes(self, nodes: list):
        for node in nodes:
            if not self.list.get(node):
                self.list[node] = []
            else:
                print("Node already exists!")
    
    # Allows you to add an edge to the graph
    def add_edge(self, node1, node2):
        if node2 not in self.list[node1]:
            self.list[node1].append(node2)
            if not self.list.get(node2):
                self.list[node2] = [node1]
            else:
                self.list[node2].append(node1)
        else:
            print("Edge already exists!")

    # Allows you to add a list of edges to the graph
    def add_edges(self, edges: list[tuple]):
        for node1, node2 in edges:
            if node2 not in self.list[node1]:
                self.list[node1].append(node2)
                if not self.list.get(node2):
                    self.list[node2] = [node1]
                else:
                    self.list[node2].append(node1)
            else:
                print("Edge already exists!")
    
    # BFS traversal: requires an input node to begin search on, and returns a list 
    # consisting of tuples, with each tuple showcasing the search order
    def bfs_traversal(self, node):
        if node in self.list:
            bfs_travel_list = []
            visited = set()
            queued = deque()
            queued.append(node)
            visited.add(node)

            while len(queued) != 0:
                vertex = queued.popleft()
                for n in self.list[vertex]:
                    if n not in visited:
                        bfs_travel_list.append((vertex, n))
                        visited.add(n)
                        queued.append(n)

            return bfs_travel_list
        
        else:
            return None

    # DFS traversal: requires an input node to begin search on, and returns a list 
    # consisting of tuples, with each tuple showcasing the search order
    def dfs_traversal(self, node):
        if node in self.list:
            dfs_travel_list = []
            visited = set()
            stack = deque()
            stack.append(node)
            visited.add(node)

            while len(stack) != 0:
                vertex = stack.pop()
                for n in self.list[vertex]:
                    if n not in visited:
                        dfs_travel_list.append((vertex, n))
                        visited.add(n)
                        stack.append(n)

            return dfs_travel_list
        
        else:
            return None
        
    # Shortest paths from node to all others: requires a start node, from which it calculates a path and distance
    # to all nodes that it can visit. Returns a dictionary tuples of each start and end node as keys, with their values
    # being another dictionary containing the keys path and distance, each storing their respective data
    def shortest_paths(self, start):
        shortest_paths = {}
        for node in self.list:
            if node != start:
                path_data = self.path(start, node)
                shortest_paths[(start, node)] = {'path': path_data[0], 'distance': path_data[1]}

        return shortest_paths

    # Path from one node to another specific node: requires input v and w which are the start and end node respectively.
    # It returns a list with the first value being a tuple storing the path traveled, and the second value being the distance
    # that it took to do so.
    def path(self, v, w):
        if v in self.list:
            visited = {}
            queued = deque()
            queued.append(v)
            visited[v] = None

            while len(queued) != 0:
                vertex = queued.popleft()

                if vertex == w:
                    path = []
                    # To ensure that the starting node isn't counted in the distance
                    distance = -1
                    while vertex is not None:
                        distance += 1
                        path.append(vertex)
                        vertex = visited[vertex]
                    
                    return [tuple(reversed(path)), distance]

                if vertex != None:
                    for n in self.list[vertex]:
                        if n not in visited:
                            visited[n] = vertex
                            queued.append(n)
        
        else:
            return None

    # Prints the adjacency list
    def print_graph(self):
        print(self.list)

    # Clears all nodes and edges from the graph
    def clear(self):
        self.list.clear()
        