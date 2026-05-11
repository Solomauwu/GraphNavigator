from .directed_graph import DirectedGraph

class UndirectedGraph(DirectedGraph):
    def add_edge(self, from_id: str, to_id: str, weight: int = 1):
        super().add_edge(from_id, to_id, weight)
        super().add_edge(to_id, from_id, weight)

    def remove_edge(self, from_id: str, to_id: str) -> bool:
        removed1 = super().remove_edge(from_id, to_id)
        removed2 = super().remove_edge(to_id, from_id)
        return removed1 or removed2

    def get_graph_type(self) -> str:
        return "undirected"

    def get_weight(self, from_id: str, to_id: str) -> int:
        if self.has_edge(from_id, to_id):
            return self._adjacency[from_id][to_id]
        if self.has_edge(to_id, from_id):
            return self._adjacency[to_id][from_id]
        return float('inf')
