from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.node = data

class Graph:
    def __init__(self) -> None:
        self.list = dict()

    # Allows you to add a vertex to the graph
    def add_node(self, node: Node):
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
    def add_edge(self, node1: Node, node2: Node):
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
    
    # BFS traversal
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

    # DFS traversal
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
    # Shortest paths from node to all others
    # Path from one node to another specific node

    # Prints the adjacency list
    def print_graph(self):
        print(self.list)

    # Clears all nodes and edges from the graph
    def clear(self):
        self.list.clear()
        