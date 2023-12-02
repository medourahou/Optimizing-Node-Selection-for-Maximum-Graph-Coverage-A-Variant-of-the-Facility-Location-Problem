from __future__ import annotations

import argparse


def parse_cmd_line() -> tuple[str, int, int, bool]:
    """Parses command line from standard input and returns the parameters.

    Returns
    -------
    str
        Path to input graph file `G`.
        
    int
        Number of nodes to select in the considered graph `G`.
    
    int
        Distance to nearest selected node to be considered as covered.
        
    bool
        Whether to plot the graph or not.
    """
    parser = argparse.ArgumentParser("Padam R&D - Technical Test")
    parser.add_argument("-i", "--in_file", help="Path to graph '*.txt' file", dest="in_file", required=True)
    parser.add_argument(
        "-n", 
        "--nb_nodes", 
        help="Number of nodes to cover the graph",
        type=int,
        dest="nb_nodes", 
        required=True,
    )
    parser.add_argument(
        "-d", 
        "--distance_to_nearest_node", 
        help="Distance to nearest selected node to be considered as covered",
        type=float, 
        dest="distance_to_nearest_node", 
        required=True,
    )
    parser.add_argument(
        "-ps", 
        "--population_size", 
        help="the population size",
        type=int, 
        dest="population_size", 
        required=True,
    )
    parser.add_argument(
        "-g", 
        "--generations", 
        help="the number of generations",
        type=int, 
        dest="generations", 
        required=True,
    )
    parser.add_argument(
        "-m", 
        "--mutation_rate", 
        help="the mutation rate",
        type=float, 
        dest="mutation_rate", 
        required=True,
    )
    parser.add_argument(
        "-p",
        "--plot",
        help="Whether to plot the graph or not",
        action="store_true",
        dest="plot_graph",
        default=False,
        required=False,
    )
    args = parser.parse_args()
    return (args.in_file, args.nb_nodes, args.distance_to_nearest_node, args.population_size, args.generations, args.mutation_rate, args.plot_graph)


def parse_file(file_name):
    """
    Parses the graph file input.

    Parameters:
    - file_name (str): Name of the file containing graph information.

    Returns:
    - tuple: Tuple containing lists of vertices and edges.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()

    num_vertices, num_edges = map(int, lines[0].split())
    vertices = [tuple(map(float, line.split())) for line in lines[1:num_vertices + 1]]
    edges = [tuple(map(int, line.split())) for line in lines[num_vertices + 1:]]

    return vertices, edges
