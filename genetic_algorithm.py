
import numpy as np
import random

class Genetic_algorithm:
    def __init__(self, graph:dict, num_nodes: int, population_size : int, generations: int, mutation_rate: float, N: int, D: float):

        """
        Initializes a Genetic Algorithm instance.

        Parameters:
        - graph (dict): A graph representation.
        - num_nodes (int): The number of nodes in the graph.
        - population_size (int): The size of the population in each generation.
        - generations (int): The number of generations to run the algorithm.
        - mutation_rate (float): The probability of mutation for each individual.
        - N (int): The number of nodes to select.
        - D (float): The distance threshold parameter.
        """

        self.graph = graph
        self.num_nodes = num_nodes
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.N = N
        self.distance_threshold =D

    
    def initialize_population(self):
        """
        Initialize the population with random sets of nodes.

        Returns:
        - list: List of sets representing the initialized population.
        """
        
        population = [set(random.sample(range(self.num_nodes), k=self.N)) for _ in range(self.population_size)]
        return population


    
    def tournament_selection(self,population, fitness_scores, tournament_size=3):
        """
        Perform tournament selection to choose parents.

        Parameters:
        - population (list): List of individuals (each individual is a set of nodes).
        - fitness_scores (list): List of fitness scores corresponding to each individual, representing the number of covered nodes for each individual
        - tournament_size (int): Number of individuals to participate in each tournament.

        Returns:
        - list: List of selected parents chosen through tournament selection.


        """
        selected_parents = []

        for _ in range(len(population)):
            tournament_indices = random.sample(range(len(population)), tournament_size)
            tournament_fitness = [fitness_scores[i] for i in tournament_indices]
            selected_index = tournament_indices[np.argmax(tournament_fitness)]
            selected_parents.append(population[selected_index])

        return selected_parents

    
    def crossover(self,parents):
        """
        Perform crossover to create offspring.

        Parameters:
        - parents (list): List of parent individuals (each element is a set of N nodes).

        Returns:
        - list: List of offspring created through crossover.

        Example:
        >>> parents = [parent1, parent2, parent3, parent4]
        >>> offspring = crossover(parents)
        >>> print(offspring)
        [child1, child2, child3, child4]

        In this example, a list of parent individuals is provided. The function performs crossover to create offspring
        by randomly selecting a crossover point and combining genetic material from the parents.
        The resulting offspring are returned as a list.
        """

        # Randomly select a crossover point
        crossover_point = random.randint(0, len(parents[0]))

        # Initialize an empty list to store offspring
        offspring = []

        # Perform crossover for each pair of parents
        for i in range(0, len(parents), 2):
            # Convert parents to lists for easy manipulation
            parent1 = list(parents[i])
            parent2 = list(parents[i + 1])

            # Create two children by combining genetic material from parents
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]

            # Add the children to the offspring list
            offspring.extend([child1, child2])

        # Return the resulting offspring
        return offspring

    
    def mutate(self,population):
        """
        Perform mutation on the population.

        Parameters:
        - population (list): List of individuals in the population.
        

        Returns:
        - list: List of individuals in the mutated population.

        Example:
        >>> population = [individual1, individual2, individual3, individual4]
        >>> mutated_population = mutate(population)
        >>> print(mutated_population)
        [mutated_individual1, mutated_individual2, mutated_individual3, mutated_individual4]

        In this example, a list of individuals is provided. The function performs mutation on each individual
        based on the specified mutation rate and total number of nodes available for mutation.
        The resulting mutated population is returned as a list.
        """

        # Initialize an empty list to store the mutated population
        mutated_population = []

        # Iterate through each individual in the population
        for individual in population:
            # Check if mutation occurs for the current individual based on the mutation rate
            if random.random() < self.mutation_rate:
                # Get the number of nodes to mutate
                num_nodes_to_mutate = random.randint(1, len(individual))

                # Remove a random number of nodes from the individual
                nodes_to_remove = random.sample(individual, num_nodes_to_mutate)
                for node in nodes_to_remove:
                    individual.remove(node)

                # Add the same number of random nodes to the individual to keep the same number of nodes in each individual
                nodes_to_add = random.sample(range(self.num_nodes), num_nodes_to_mutate)
                individual.extend(nodes_to_add)

            # Add the mutated individual to the mutated population
            mutated_population.append(individual)

        # Return the resulting mutated population
        return mutated_population


    
    
    def replace_population(self,old_population, new_population, old_fitness_scores, new_fitness_scores):
        """
        Replace old population with new population based on fitness.

        Parameters:
        - old_population (list): List of individuals (chromosomes) from the old population.
        - new_population (list): List of individuals from the new population.
        - old_fitness_scores (list): List of fitness scores corresponding to individuals in the old population.
        - new_fitness_scores (list): List of fitness scores corresponding to individuals in the new population.

        Returns:
        - list: List of individuals in the new population replacing the old population.

        Example:
        >>> old_population = [old_individual1, old_individual2, old_individual3]
        >>> new_population = [new_individual1, new_individual2, new_individual3]
        >>> old_fitness_scores = [8, 6, 9]
        >>> new_fitness_scores = [7, 5, 8]
        >>> updated_population = replace_population(old_population, new_population, old_fitness_scores, new_fitness_scores)
        >>> print(updated_population)
        [new_individual3, old_individual1, new_individual1]

        In this example, lists of individuals and their corresponding fitness scores from both old and new populations are provided.
        The function replaces the old population with the new population based on fitness scores.
        The resulting updated population is returned as a list.
        """

        # Combine individuals and fitness scores from old and new populations
        combined_population = old_population + new_population
        combined_fitness_scores = old_fitness_scores + new_fitness_scores

        # Sort the combined population indices based on fitness scores in descending order
        sorted_indices = np.argsort(combined_fitness_scores)[::-1]

        # Select individuals from the combined population to form the new population
        updated_population = [combined_population[i] for i in sorted_indices[:len(old_population)]]

        # Return the resulting updated population
        return updated_population


    
    def genetic_algorithm_for_node_coverage(self):
        """
        The function performs a genetic algorithm to find the
        best solution (set of nodes) that maximizes node coverage within the specified distance threshold.
        The best solution is returned as a set of nodes.

        Parameters:
        - graph (Graph): Graph object representing the network.

        Returns:
        - list: Best solution (set of nodes) found by the genetic algorithm.

        """

        
        # Initialize the population
        population = self.initialize_population()

        for generation in range(self.generations):
            # Evaluate the fitness of each individual in the population
            fitness_scores = [len(self.graph.compute_node_coverage(node_set, self.distance_threshold)) for node_set in population]

            # Select individuals for reproduction using tournament selection
            selected_parents = self.tournament_selection(population, fitness_scores)

            # Create offspring through crossover
            offspring = self.crossover(selected_parents)

            # Apply mutation to the offspring
            mutated_offspring = self.mutate(offspring)

            # Evaluate the fitness of the offspring
            offspring_fitness_scores = [len(self.graph.compute_node_coverage(node_set, self.distance_threshold)) for node_set in mutated_offspring]

            # Replace the old population with the new population
            population = self.replace_population(population, mutated_offspring, fitness_scores, offspring_fitness_scores)

            # Optional: You can print or log the best fitness in each generation
            best_fitness = max(fitness_scores)
            print(f"Generation {generation + 1}, number of nodes covered: {best_fitness}")

        # Select the best solution from the final population
        best_solution_index = np.argmax(fitness_scores)
        best_solution = population[best_solution_index]

        return best_solution
