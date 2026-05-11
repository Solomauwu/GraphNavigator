from typing import Dict, List, Optional
from .base_graph import BaseGraph
from .graph_node import GraphNode

class DirectedGraph(BaseGraph):
    def __init__(self):
        self._nodes: Dict[str, GraphNode] = {}
        self._adjacency: Dict[str, Dict[str, int]] = {}

    def add_node(self, node: GraphNode):
        if node.id not in self._nodes:
            self._nodes[node.id] = node
            self._adjacency[node.id] = {}

    def remove_node(self, node_id: str) -> bool:
        if node_id not in self._nodes:
            return False

        del self._nodes[node_id]
        del self._adjacency[node_id]

        for edges in self._adjacency.values():
            if node_id in edges:
                del edges[node_id]

        return True

    def add_edge(self, from_id: str, to_id: str, weight: int = 1):
        if from_id not in self._nodes:
            raise ValueError(f"Node {from_id} does not exist")
        if to_id not in self._nodes:
            raise ValueError(f"Node {to_id} does not exist")
        if weight <= 0:
            raise ValueError("Weight must be positive")

        self._adjacency[from_id][to_id] = weight

    def remove_edge(self, from_id: str, to_id: str) -> bool:
        if from_id in self._adjacency and to_id in self._adjacency[from_id]:
            del self._adjacency[from_id][to_id]
            return True
        return False

    def get_node(self, node_id: str) -> Optional[GraphNode]:
        return self._nodes.get(node_id)

    def get_all_nodes(self) -> List[GraphNode]:
        return list(self._nodes.values())

    def get_adjacency_list(self) -> Dict:
        return self._adjacency

    def has_node(self, node_id: str) -> bool:
        return node_id in self._nodes

    def has_edge(self, from_id: str, to_id: str) -> bool:
        return from_id in self._adjacency and to_id in self._adjacency[from_id]

    def get_graph_type(self) -> str:
        return "directed"

    def clear(self):
        self._nodes.clear()
        self._adjacency.clear()

    def get_weight(self, from_id: str, to_id: str) -> int:
        if self.has_edge(from_id, to_id):
            return self._adjacency[from_id][to_id]
        return float('inf')
