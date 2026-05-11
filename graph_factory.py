from models.directed_graph import DirectedGraph
from models.undirected_graph import UndirectedGraph
from models.weighted_graph import WeightedGraph

class GraphFactory:
    @staticmethod
    def create_graph(graph_type: str):
        graph_type = graph_type.lower()
        if graph_type == "directed":
            return DirectedGraph()
        elif graph_type == "undirected":
            return UndirectedGraph()
        elif graph_type == "weighted":
            return WeightedGraph()
        else:
            raise ValueError(f"Unknown graph type: {graph_type}. Use: directed, undirected, weighted")
