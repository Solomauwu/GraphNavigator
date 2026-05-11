import json
import os
from models.graph_node import GraphNode

FILE_NAME = "graph_data.json"

def save_graph(graph):
    data = {
        "graph_type": graph.get_graph_type(),
        "nodes": [],
        "edges": []
    }

    for node in graph.get_all_nodes():
        data["nodes"].append({"id": node.id, "name": node.name})

    adjacency = graph.get_adjacency_list()
    for from_id, edges in adjacency.items():
        for to_id, weight in edges.items():
            data["edges"].append({
                "from": from_id,
                "to": to_id,
                "weight": weight
            })

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_graph():
    if not os.path.exists(FILE_NAME):
        return None, None, None

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("graph_type"), data.get("nodes", []), data.get("edges", [])
