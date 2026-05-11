"""
Graph Navigator - Console Application for Graph Operations
Author: Student Name
"""

from controllers.graph_controller import GraphController

def main():
    print("\n" + "=" * 50)
    print("     WELCOME TO GRAPH NAVIGATOR")
    print("=" * 50)
    print("A tool for graph creation, traversal, and pathfinding")
    print("Supports: Directed, Undirected, Weighted graphs")
    print("Algorithms: BFS, DFS, Dijkstra")
    print("=" * 50)

    controller = GraphController()
    controller.run()

if __name__ == "__main__":
    main()
