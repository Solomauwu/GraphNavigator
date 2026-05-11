from .directed_graph import DirectedGraph

class WeightedGraph(DirectedGraph):
    def add_edge(self, from_id: str, to_id: str, weight: int = 1):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        super().add_edge(from_id, to_id, weight)

    def get_graph_type(self) -> str:
        return "weighted"
