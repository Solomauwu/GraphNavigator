from models.graph_node import GraphNode
from factories.graph_factory import GraphFactory
from algorithms.traversal import bfs, dfs
from algorithms.shortest_path import find_shortest_path
from services import json_storage
from views import console_view as view

class GraphController:
    def __init__(self):
        self.graph = None

    def run(self):
        while True:
            view.show_menu()
            choice = input("Your choice: ").strip()

            if choice == "1":
                self.create_graph()
            elif choice == "2":
                self.add_node()
            elif choice == "3":
                self.add_edge()
            elif choice == "4":
                self.remove_node()
            elif choice == "5":
                self.remove_edge()
            elif choice == "6":
                self.show_graph()
            elif choice == "7":
                self.bfs_traversal()
            elif choice == "8":
                self.dfs_traversal()
            elif choice == "9":
                self.shortest_path()
            elif choice == "10":
                self.save_graph()
            elif choice == "11":
                self.load_graph()
            elif choice == "12":
                self.show_info()
            elif choice == "0":
                view.show_message("Goodbye!")
                break
            else:
                view.show_message("Invalid choice!", True)

    def create_graph(self):
        graph_type = view.get_graph_type()
        self.graph = GraphFactory.create_graph(graph_type)
        view.show_message(f"Created new {graph_type} graph")

    def add_node(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return

        node_id, name = view.get_node_info()
        if not node_id or not name:
            view.show_message("ID and name cannot be empty!", True)
            return

        if self.graph.has_node(node_id):
            view.show_message(f"Node with ID '{node_id}' already exists!", True)
            return

        node = GraphNode(node_id, name)
        self.graph.add_node(node)
        view.show_message(f"Node '{node}' added")

    def add_edge(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return

        has_weight = self.graph.get_graph_type() == "weighted"
        from_id, to_id, weight = view.get_edge_info(has_weight)

        if not self.graph.has_node(from_id):
            view.show_message(f"Node '{from_id}' not found!", True)
            return
        if not self.graph.has_node(to_id):
            view.show_message(f"Node '{to_id}' not found!", True)
            return

        try:
            self.graph.add_edge(from_id, to_id, weight)
            view.show_message(f"Edge added: {from_id} -> {to_id} (weight: {weight})")
        except ValueError as e:
            view.show_message(str(e), True)

    def remove_node(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return

        node_id = input("Enter node ID to remove: ").strip()
        if self.graph.remove_node(node_id):
            view.show_message(f"Node '{node_id}' removed")
        else:
            view.show_message(f"Node '{node_id}' not found!", True)

    def remove_edge(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return

        from_id = input("Enter source node ID: ").strip()
        to_id = input("Enter target node ID: ").strip()

        if self.graph.remove_edge(from_id, to_id):
            view.show_message(f"Edge removed: {from_id} -> {to_id}")
        else:
            view.show_message("Edge not found!", True)

    def show_graph(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return
        view.show_graph(self.graph)

    def bfs_traversal(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return

        start_id = input("Enter start node ID: ").strip()
        if not self.graph.has_node(start_id):
            view.show_message("Node not found!", True)
            return

        try:
            result = bfs(self.graph, start_id)
            view.show_traversal_result(result)
        except ValueError as e:
            view.show_message(str(e), True)

    def dfs_traversal(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return

        start_id = input("Enter start node ID: ").strip()
        if not self.graph.has_node(start_id):
            view.show_message("Node not found!", True)
            return

        try:
            result = dfs(self.graph, start_id)
            view.show_traversal_result(result)
        except ValueError as e:
            view.show_message(str(e), True)

    def shortest_path(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return

        start_id = input("Enter start node ID: ").strip()
        end_id = input("Enter end node ID: ").strip()

        if not self.graph.has_node(start_id):
            view.show_message("Start node not found!", True)
            return
        if not self.graph.has_node(end_id):
            view.show_message("End node not found!", True)
            return

        try:
            path, distance = find_shortest_path(self.graph, start_id, end_id)
            view.show_path_result(path, distance)
        except ValueError as e:
            view.show_message(str(e), True)

    def save_graph(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return

        json_storage.save_graph(self.graph)
        view.show_message("Graph saved to graph_data.json")

    def load_graph(self):
        graph_type, nodes_data, edges_data = json_storage.load_graph()
        if not graph_type:
            view.show_message("No saved graph found!", True)
            return

        self.graph = GraphFactory.create_graph(graph_type)

        # Add nodes
        for node_data in nodes_data:
            node = GraphNode(node_data["id"], node_data["name"])
            self.graph.add_node(node)

        # Add edges
        for edge_data in edges_data:
            try:
                self.graph.add_edge(edge_data["from"], edge_data["to"], edge_data.get("weight", 1))
            except ValueError:
                pass

        view.show_message(f"Graph loaded from graph_data.json ({len(nodes_data)} nodes, {len(edges_data)} edges)")

    def show_info(self):
        if not self.graph:
            view.show_message("Create a graph first!", True)
            return
        view.show_graph_info(self.graph)
