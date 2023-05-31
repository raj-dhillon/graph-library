from graph import Graph as g

DONE = False

# Main loop of the program
def load_program():
    graph = g()
    print("\nWelcome to the graph library application!\n")
    while not DONE:
        display_options()
        process_input(graph)

# Displays the menu to the user
def display_options():
    print("Please select an option below:")
    print("1. Insert a singular node.")
    print("2. Insert multiple nodes.")
    print("3. Insert an edge.")
    print("4. Print graph.")
    print("5. BFS graph traversal.")
    print("6. DFS graph traversal.")
    print("7. Shortest path from node to all others.")
    print("8. Shortest path from node u to node v.")
    print("9. Clear graph.")
    print("10. Exit program.\n")

# Processes the user input, and completes their request
def process_input(graph: g):
    selection = input("Selection (1-10): ")
    if selection.isnumeric():
        selection = int(selection)
    else:
        print("Please enter valid input!\n")
        return
    
    match selection:
        case 1:
            graph.add_node(input("Enter node: "))

        case 2:
            graph.add_nodes(input("Enter nodes (separate by ','): "))

        case 3:
            edges = input("Enter two edges (separate by ','): ")
            edges = edges.split(',')
            if len(edges) != 2:
                print("Incorrect input!")
            else:
                for n in edges:
                    n.strip()
                graph.add_edge(edges[0], edges[1])

        case 4:
            graph.print_graph()

        case 5:
            node = input("Enter a node: ")
            print(graph.bfs_traversal(node))

        case 6:
            node = input("Enter a node: ")
            print(graph.dfs_traversal(node))

        case 7:
            node = input("Enter a node: ")
            print(graph.shortest_paths(node))

        case 8:
            nodes = input("Enter two nodes (separate by ','): ")
            nodes = nodes.split(',')
            if len(nodes) != 2:
                print("Incorrect input!")
            else:
                for n in nodes:
                    n.strip()
                print(graph.path(nodes[0], nodes[1]))

        case 9:
            graph.clear()

        case 10:
            print("EXITING!")
            DONE = True
            exit()

        case _:
            print("Incorrect selection!")
        
    print("\n")


# runs the program
load_program()