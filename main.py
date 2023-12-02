
from graph import Graph
from genetic_algorithm import Genetic_algorithm
from input import parse_cmd_line, parse_file
import math
import time

def main():
    """Entry point of this technical test. It fetches the selected instance's information and processes it."""
    in_file, N, D,population_size,nb_generations,mutation_rate, plot_graph = parse_cmd_line()
    print(f"Loading graph '{in_file}' - Algorithm settings 'N = {N}' and 'D = {D}'")
    vertices, edges = parse_file(in_file)
    print(f"Graph has {len(edges)} edges and {len(vertices)} vertices")
    
    graph = Graph(vertices, edges)
   
    genetic_algo = Genetic_algorithm(graph,len(graph.vertices),population_size,nb_generations,mutation_rate,N,D)
    
    start_time = time.time()
    print("genetic algorithm running....")
    genetic_algo.genetic_algorithm_for_node_coverage()
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Time taken: {elapsed_time} seconds")

    if plot_graph:
        graph.plot()

    

if __name__ == "__main__":
    main()
