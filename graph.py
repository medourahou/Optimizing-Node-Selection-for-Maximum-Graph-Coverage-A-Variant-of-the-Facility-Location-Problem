import argparse
import random
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np



class Graph:
    """
    Class used to describe a graph with a list of vertices and a list of edges between those vertices.
    """

    def __init__(self, vertices, edges):
        """
        Basic constructor of the `Graph` class.

        Parameters:
        - vertices (list): List of vertices, each represented by a tuple of coordinates.
        - edges (list): List of edges, each represented by a tuple (vertex1, vertex2, distance).

        Attributes:
        - vertices (list): List of vertices, each represented by a tuple of coordinates.
        - edges (list): List of edges, each represented by a tuple (vertex1, vertex2, distance).
        - node_info (dict): Dictionary to store the cordinates of each node.
        - adjacency_list (dict): Adjacency list for fast neighbor lookups.
        """
        self.vertices = vertices
        self.edges = edges
        self.node_info = {}  # Dictionary to store information about each node
        self.adjacency_list = {}  # Adjacency list for fast neighbor lookups
        self.initialize_graph()

    def initialize_graph(self):
        """
        Initialize the graph by populating node_info and adjacency_list.

        Parameters:
        - vertices (list): List of vertices, each represented by a tuple of coordinates.
        - edges (list): List of edges, each represented by a tuple (vertex1, vertex2, distance).
        """
        # Initialize node_info with coordinates for each node
        for vertex_id, coordinates in enumerate(self.vertices):
            self.node_info[vertex_id] = {'coordinates': coordinates}

        # Build adjacency list and edge_info
        for edge in self.edges:
            vertex1, vertex2, distance = edge[:3]

            # Update adjacency list
            if vertex1 not in self.adjacency_list:
                self.adjacency_list[vertex1] = []
            if vertex2 not in self.adjacency_list:
                self.adjacency_list[vertex2] = []

            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

        # Add distance information to node_info
        for vertex1, vertex2, distance in self.edges:
            if 'edges' not in self.node_info[vertex1]:
                self.node_info[vertex1]['edges'] = {}
            if 'edges' not in self.node_info[vertex2]:
                self.node_info[vertex2]['edges'] = {}

            self.node_info[vertex1]['edges'][vertex2] = distance
            self.node_info[vertex2]['edges'][vertex1] = distance

    def get_coordinates(self, node):
        """
        Get the coordinates of a given node.

        Parameters:
        - node: Node identifier.

        Returns:
        - tuple: Coordinates of the given node.
        """
        return self.node_info[node]['coordinates']

    def get_neighbors(self, node):
        """
        Get the neighbors of a given node.

        Parameters:
        - node: Node identifier.

        Returns:
        - list: List of neighboring nodes.
        """
        return self.adjacency_list.get(node, [])

    def get_distance(self, node1, node2):
        """
        Get the distance between two nodes.

        Parameters:
        - node1: First node identifier.
        - node2: Second node identifier.

        Returns:
        - float: Distance between the given nodes.
        """
        return self.node_info[node1]['edges'][node2]

    def plot(self):
        """
        Plots the graph, highlighting edges based on their distances.
        """
        distances = list(set(edge[2] for edge in self.edges))
        colors = plt.cm.get_cmap("viridis", len(distances))
        _, ax = plt.subplots()
        for i, distance in enumerate(distances):
            lines = [[self.vertices[edge[0]], self.vertices[edge[1]]] for edge in self.edges if edge[2] == distance]
            ax.add_collection(LineCollection(lines, colors=colors(i), alpha=0.7, label=f"distance {distance}"))
        ax.scatter(*zip(*self.vertices), c='red', label='Vertices')
        ax.plot()
        ax.legend()
        plt.title(f"#E={len(self.edges)}, #V={len(self.vertices)}")
        plt.show()

    def dfs_coverage(self, start_node, distance_threshold):
        """
        Computes coverage of nodes from a given starting node within a distance threshold.

        Parameters:
        - start_node: Node identifier to start the coverage computation.
        - distance_threshold: Maximum distance for coverage.

        Returns:
        - set: Set of nodes covered within the specified distance threshold.
        """
        visited = set()

        def dfs(node, distance):
            nonlocal visited

            visited.add(node)

            for neighbor in self.get_neighbors(node):
                if neighbor not in visited and self.get_distance(node, neighbor) <= distance:
                    dfs(neighbor, distance - self.get_distance(node, neighbor))

        dfs(start_node, distance_threshold)
        return visited - {start_node}

    def compute_node_coverage(self, node_set, D):
        """
        Computes coverage for each node in a given set.

        Parameters:
        - node_set: Set of nodes for which coverage needs to be computed.
        - D: Maximum distance for coverage.

        Returns:
        - set: Union of coverage sets for all nodes in the input set.
        """
        node_coverages = []

        for vertex_id in node_set:
            coverage = self.dfs_coverage(vertex_id, D)
            node_coverages.append(coverage)

        return set().union(*node_coverages)

