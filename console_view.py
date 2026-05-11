def show_menu():
    print("\n" + "=" * 40)
    print("        GRAPH NAVIGATOR")
    print("=" * 40)
    print("1. Create New Graph")
    print("2. Add Node")
    print("3. Add Edge")
    print("4. Remove Node")
    print("5. Remove Edge")
    print("6. Show Graph")
    print("7. BFS Traversal")
    print("8. DFS Traversal")
    print("9. Find Shortest Path")
    print("10. Save Graph")
    print("11. Load Graph")
    print("12. Show Graph Info")
    print("0. Exit")
    print("-" * 40)


def get_graph_type():
    print("\nSelect graph type:")
    print("1. Directed")
    print("2. Undirected")
    print("3. Weighted")
    choice = input("Choice: ")

    if choice == "1":
        return "directed"
    elif choice == "2":
        return "undirected"
    elif choice == "3":
        return "weighted"
    else:
        return "directed"


def get_node_info():
    node_id = input("Enter node ID: ").strip()
    name = input("Enter node name: ").strip()
    return node_id, name


def get_edge_info(has_weight=False):
    from_id = input("Enter source node ID: ").strip()
    to_id = input("Enter target node ID: ").strip()
    weight = 1
    if has_weight:
        try:
            weight = int(input("Enter weight: ").strip())
        except ValueError:
            weight = 1
    return from_id, to_id, weight


def show_graph(graph):
    print("\n" + "=" * 40)
    print(f"Graph Type: {graph.get_graph_type()}")
    print("-" * 40)

    nodes = graph.get_all_nodes()
    if not nodes:
        print("No nodes in graph")
        return

    print("Nodes:")
    for node in nodes:
        print(f"  • {node}")

    print("\nEdges:")
    adjacency = graph.get_adjacency_list()
    has_edges = False
    for from_id, edges in adjacency.items():
        for to_id, weight in edges.items():
            from_node = graph.get_node(from_id)
            to_node = graph.get_node(to_id)
            print(f"  {from_node} -> {to_node} (weight: {weight})")
            has_edges = True

    if not has_edges:
        print("  No edges")


def show_traversal_result(nodes):
    print("\nTraversal result:")
    for i, node in enumerate(nodes):
        print(f"  {i+1}. {node}")


def show_path_result(path, distance):
    if not path or distance == -1:
        print("\nNo path found between the nodes!")
        return

    print(f"\nShortest path (distance: {distance}):")
    arrow = " -> "
    print(f"  {arrow.join(str(node) for node in path)}")


def show_graph_info(graph):
    print("\n" + "=" * 40)
    print("GRAPH INFORMATION")
    print("=" * 40)
    print(f"Type: {graph.get_graph_type()}")
    print(f"Number of nodes: {len(graph.get_all_nodes())}")

    edge_count = sum(len(edges) for edges in graph.get_adjacency_list().values())
    print(f"Number of edges: {edge_count}")

    if graph.get_graph_type() == "weighted":
        total_weight = 0
        for edges in graph.get_adjacency_list().values():
            total_weight += sum(edges.values())
        print(f"Total weight sum: {total_weight}")


def show_message(msg, is_error=False):
    if is_error:
        print(f"\n[ERROR] {msg}")
    else:
        print(f"\n[OK] {msg}")
