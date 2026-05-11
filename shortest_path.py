from collections import deque
from typing import List, Tuple
import heapq

def find_shortest_path(graph, start_id: str, end_id: str) -> Tuple[List, int]:
    if not graph.has_node(start_id) or not graph.has_node(end_id):
        raise ValueError("Start or end node not found")

    # Check if graph has weights > 1 (use Dijkstra)
    has_weights = False
    adj = graph.get_adjacency_list()
    for edges in adj.values():
        for weight in edges.values():
            if weight != 1:
                has_weights = True
                break

    if graph.get_graph_type() == "weighted" or has_weights:
        return _dijkstra(graph, start_id, end_id)
    else:
        return _bfs_unweighted(graph, start_id, end_id)


def _dijkstra(graph, start_id: str, end_id: str) -> Tuple[List, int]:
    distances = {node.id: float('inf') for node in graph.get_all_nodes()}
    previous = {node.id: None for node in graph.get_all_nodes()}
    distances[start_id] = 0

    pq = [(0, start_id)]

    while pq:
        current_dist, current_id = heapq.heappop(pq)

        if current_id == end_id:
            break

        if current_dist > distances[current_id]:
            continue

        adj = graph.get_adjacency_list()
        if current_id in adj:
            for neighbor_id, weight in adj[current_id].items():
                new_dist = current_dist + weight
                if new_dist < distances[neighbor_id]:
                    distances[neighbor_id] = new_dist
                    previous[neighbor_id] = current_id
                    heapq.heappush(pq, (new_dist, neighbor_id))

    if distances[end_id] == float('inf'):
        return [], -1

    # Reconstruct path
    path = []
    node_id = end_id
    while node_id is not None:
        path.insert(0, graph.get_node(node_id))
        node_id = previous[node_id]

    return path, distances[end_id]


def _bfs_unweighted(graph, start_id: str, end_id: str) -> Tuple[List, int]:
    queue = deque()
    visited = set()
    previous = {}

    queue.append(start_id)
    visited.add(start_id)
    previous[start_id] = None

    while queue:
        current_id = queue.popleft()

        if current_id == end_id:
            break

        adj = graph.get_adjacency_list()
        if current_id in adj:
            for neighbor_id in adj[current_id].keys():
                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    previous[neighbor_id] = current_id
                    queue.append(neighbor_id)

    if end_id not in previous:
        return [], -1

    # Reconstruct path
    path = []
    node_id = end_id
    while node_id is not None:
        path.insert(0, graph.get_node(node_id))
        node_id = previous[node_id]

    return path, len(path) - 1
