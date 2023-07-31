import random


class Environment:
    def __init__(self):
        # Graph represented as a dictionary of nodes to their neighbors
        self.graph = {}

        # Create a loop of nodes
        for i in range(1, 41):
            self.add_edge(i, i % 40 + 1)

        # Add ten additional edges
        added_edges = 0
        while added_edges < 10:
            node1 = random.randint(1, 40)
            node2 = random.randint(1, 40)
            if node1 != node2 and node2 not in self.graph.get(node1, []) \
                    and len(self.graph.get(node1, [])) < 3 and len(self.graph.get(node2, [])) < 3:
                self.add_edge(node1, node2)
                added_edges += 1

    def add_edge(self, node1, node2):
        # Adds an edge between the given nodes in the graph
        # If the nodes do not exist, they are added to the graph
        self.graph.setdefault(node1, []).append(node2)
        self.graph.setdefault(node2, []).append(node1)

    def get_neighbors(self, node):
        # Returns the neighbors of the given node in the graph
        # If the node does not exist, returns an empty list
        return self.graph.get(node, [])
