class GraphNode:
    def __init__(self, node_id: str, name: str):
        self.id = node_id
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.id})"

    def __eq__(self, other):
        return isinstance(other, GraphNode) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    @staticmethod
    def from_dict(data):
        return GraphNode(data["id"], data["name"])
