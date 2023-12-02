# Genetic Algorithm for Node Coverage in Graphs

## I. Introduction

In tackling this multifaceted problem, I employ a genetic algorithm, a heuristic optimization technique inspired by the process of natural selection. This algorithm iteratively refines sets of nodes, evolving towards optimal solutions for maximizing coverage. The incorporation of genetic algorithms introduces adaptability and efficiency, enabling the algorithm to navigate through vast solution spaces and converge on solutions that represent significant improvements in node coverage.



## II. Implementation

### Input Parsing

The project parses command line arguments for configuration, including the input graph file, number of nodes, maximum distance, population size, generations, mutation rate, and whether to plot the graph.

### Graph Representation

The Graph class represents the graph using an adjacency list to expedite graph traversal. This optimization enhances the efficiency of operations that involve navigating the graph structure. Additionally, the class employs the Depth-First Search (DFS) algorithm to identify covered nodes within the specified distance threshold. DFS is a fundamental algorithm for exploring and discovering connected nodes in the graph, contributing to the overall efficiency of the coverage calculation process.


### Genetic Algorithm

The Genetic_algorithm class serves as the engine for the optimization process, implementing a customized genetic algorithm tailored to address the challenges posed by this variant of Facility Location Problem (FLP). The algorithm undergoes several key stages to iteratively refine solutions and converge on an optimal set of nodes for maximizing coverage within the defined distance threshold.

1. **Initialization of Populations:** The algorithm begins by initializing a population of potential solutions. Each solution represents a set of nodes within the graph.

2. **Parent Selection through Tournament Selection:** To promote diversity and select promising individuals, the algorithm employs tournament selection. Multiple individuals are randomly chosen from the population, and the one with the highest fitness score (indicating better coverage) is selected as a parent. This process is repeated to form a group of parents for the next steps.

3. **Crossover Operation:** Crossover mimics the natural process of genetic recombination. Pairs of parents are chosen, and a random crossover point is selected. Genetic material before the crossover point is exchanged between parents, producing two offspring. This operation introduces exploration and recombination of genetic material to generate new solutions.

4. **Mutation Operation:** To further explore the solution space, the algorithm introduces controlled mutations. Randomly selected individuals undergo mutation, where a subset of nodes is altered. This operation adds a level of randomness and diversity to the population, preventing premature convergence to suboptimal solutions.

5. **Replacement of Populations based on Fitness Scores:** The algorithm evaluates the fitness of individuals in both the parent and offspring populations. Fitness, in this context, represents the number of covered nodes within the specified distance threshold. The populations are then dynamically replaced, favoring individuals with higher fitness scores. This process ensures that the population evolves towards better solutions over successive generations.

These sequential steps, executed iteratively over multiple generations, allow the genetic algorithm to explore and exploit the solution space effectively. The interplay of selection, crossover, and mutation operations, coupled with the dynamic replacement of populations based on fitness, enables the algorithm to adapt and converge towards solutions that represent a maximal coverage of nodes within the specified distance threshold.


## Execution

The `main` function orchestrates the execution, loading the graph, initializing the genetic algorithm, and running it. Execution time is recorded and displayed.

## Usage

To run the project using command line:

```bash
python3 main.py -i <input_file> -n <num_nodes> -d <distance_threshold> -ps <population_size> -g <generations> -m <mutation_rate> -p
```
Example: 
```
python3 main.py -i ./instances/islands.txt -n 10 -d 25 -ps 60 -g 1 -m 0.8
```
## III. Results

The algorithm is tested with 2 instances islands.txt and paris_map.txt, Some results are shown in the two tables below:

<br>
<center> with islands.txt </center>
<br>

| N   | D     | nb of covered nodes | CPU time (s)   | Population size | nb of generations   |
|------|----------|-----|------------|------------|----------|
| 10  | 25     | 60/60  | 0.10        | 60   | 1  |
| 20  | 30     | 60/60  | 0.17     | 60   | 1  |
| 30  | 30     | 60/60  | 0.25         | 60  | 1  |

<br>
<center> with paris_map.txt </center>
<br>

| N   | D     | nb of covered nodes | CPU time (s)   | Population size | nb of generations   |
|------|----------|-----|------------|------------|----------|
| 10  | 25     | 4528/11348  | 255.58        | 200   | 50  |
| 100  | 50     | 11345/11348  | 741.29    | 200   | 10  |

## IV. Analysis


Key Observations:

1. **Coverage Performance:**
   - Across both instances ("islands.txt" and "paris_map.txt"), the algorithm consistently achieves notable coverage, indicating its efficacy in selecting nodes within the specified distance thresholds.
   - The coverage results are particularly impressive for the "paris_map.txt" instance, where a substantial portion of nodes is covered, demonstrating the algorithm's capability to handle more complex geographical demands.

2. **Computational Efficiency:**
   - The algorithm exhibits computational efficiency, especially in the "islands.txt" instance, where it quickly converges to optimal solutions within a single generation.
   - The longer CPU times observed for the "paris_map.txt" instance are expected given its larger graph size and varied configurations. Despite this, the algorithm still demonstrates effectiveness in covering a significant number of nodes.

3. **Hyperparameter Considerations:**
   - The choice of hyperparameters, including population size and number of generations, appears well-suited for the characteristics of each instance. The algorithm adapts its behavior based on the complexity of the problem.
   - The mutation rate value choosed is crucial for maintaining genetic diversity. A well-chosen mutation rate ensures exploration of new solutions without compromising the stability of the population.

4. **Scalability:**
   - The algorithm demonstrates scalability by successfully handling instances with varying graph sizes, node numbers, and distance thresholds.
   - The ability to adapt to different scenarios, as seen in both instances, highlights the algorithm's flexibility in addressing diverse Facility Location Problems.



The presented results affirm the algorithm's effectiveness in addressing Facility Location Problems through a genetic algorithm approach. Its consistent coverage across instances, coupled with computational efficiency, showcases its potential for real-world applications. The algorithm's scalability allows it to handle instances of varying complexities, making it a versatile tool for optimizing node placement in geographical demand scenarios.

## V. Conclusion

In conclusion, while the algorithm demonstrates strong performance, further exploration and refinement can contribute to its continual improvement and applicability across a broader spectrum of Facility Location Problems:

# todo
1. **Fine-Tuning Hyperparameters:**
   - Conduct further experiments to fine-tune hyperparameters, including the mutation rate, for optimal performance in specific scenarios.
   - Explore the impact of different population sizes and numbers of generations on the algorithm's convergence and coverage.

2. **Additional Instance Testing:**
   - Test the algorithm on a broader range of instances to evaluate its generalizability and robustness across diverse Facility Location Problems.

3. **Comparison with Other Approaches:**
   - Conduct comparative analyses with other optimization approaches to benchmark the algorithm's performance against alternative methods.

