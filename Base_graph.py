from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class BaseGraph(ABC):
    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def remove_node(self, node_id: str) -> bool:
        pass

    @abstractmethod
    def add_edge(self, from_id: str, to_id: str, weight: int = 1):
        pass

    @abstractmethod
    def remove_edge(self, from_id: str, to_id: str) -> bool:
        pass

    @abstractmethod
    def get_node(self, node_id: str):
        pass

    @abstractmethod
    def get_all_nodes(self) -> List:
        pass

    @abstractmethod
    def get_adjacency_list(self) -> Dict:
        pass

    @abstractmethod
    def has_node(self, node_id: str) -> bool:
        pass

    @abstractmethod
    def has_edge(self, from_id: str, to_id: str) -> bool:
        pass

    @abstractmethod
    def get_graph_type(self) -> str:
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_weight(self, from_id: str, to_id: str) -> int:
        pass
