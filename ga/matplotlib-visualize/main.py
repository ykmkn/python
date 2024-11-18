import random
from utils.genetic_helpers import genetic_algorithm
from utils.visualize import visualize_generation
# first generation
generation = [[0,0,1,0,1],[1,0,0,0,1],[0,1,0,0,0],[1,0,0,0,0],[0,1,0,1,1]]
# number of generations
num_of_generation = 50
# list of operations
operations =["SELECTION","CROSSOVER","MUTATION"]
# probabilities of the operations
operation_probabilities = [0.4, 0.5, 0.1]

fitness_scores = genetic_algorithm(generation, num_of_generation, operations, operation_probabilities)
visualize_generation(fitness_scores)
