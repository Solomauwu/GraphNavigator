from collections import deque
from typing import List

def bfs(graph, start_id: str) -> List:
    if not graph.has_node(start_id):
        raise ValueError(f"Node {start_id} not found")

    visited = set()
    queue = deque()
    result = []

    queue.append(start_id)
    visited.add(start_id)

    while queue:
        current_id = queue.popleft()
        result.append(graph.get_node(current_id))

        adjacency = graph.get_adjacency_list()
        if current_id in adjacency:
            for neighbor_id in adjacency[current_id].keys():
                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    queue.append(neighbor_id)

    return result


def dfs(graph, start_id: str) -> List:
    if not graph.has_node(start_id):
        raise ValueError(f"Node {start_id} not found")

    visited = set()
    result = []

    def dfs_recursive(node_id: str):
        visited.add(node_id)
        result.append(graph.get_node(node_id))

        adjacency = graph.get_adjacency_list()
        if node_id in adjacency:
            for neighbor_id in adjacency[node_id].keys():
                if neighbor_id not in visited:
                    dfs_recursive(neighbor_id)

    dfs_recursive(start_id)
    return result
