import random
# first generation
generation = [[0,0,1,0,1],[1,0,0,0,1],[0,1,0,0,0],[1,0,0,0,0],[0,1,0,1,1]]
# number of generations
num_of_generation = 30
# list of operations
operations =["SELECTION","CROSSOVER","MUTATION"]
# probabilities of the operations
operation_probabilities = [0.3, 0.5, 0.2]

def evaluate(numb_list):
    """ This function evaluates the sum of the elements in the list numb_list
    """
    return sum(numb_list)

def evaluate_generation(generation):
    """ This function evaluates the generation
    """
    evaluated_values = []
    for i in range(len(generation)):
        evaluated_values.append(evaluate(generation[i]))
    return evaluated_values

def select_with_probability(list, probabilities):
    """ This function selects an element from the list list with the probabilities probabilities
    """
    return random.choices(list, weights=probabilities, k=1)[0]

def print_individual(individual):
    """ This function prints the individual and its evaluation
    """
    print("Individual: ",individual," Evaluation: ",evaluate(individual))

def print_generation(generation):
    """ This function prints the generation
    """
    for i in range(len(generation)):
        print_individual(generation[i])

def add_individual_to_generation(generation, individual):
    """ This function adds an individual to the generation
    """
    generation.append(individual)

def mutate(individual):
    """ This function mutates the individual
    """
    index = random.randint(0, len(individual)-1)
    individual[index] = 1 - individual[index]
    return individual

# create a next generation from the current generation
for i in range(num_of_generation):

    # print current generation
    print_generation(generation)

    # evaluate the current generation
    evaluated_values = evaluate_generation(generation)

    # create a next generation from the current generation
    next_generation = []
    for i in range(len(generation)):
        selected_operation=select_with_probability(operations, operation_probabilities)
        print("Selected operation: ",selected_operation)

        if selected_operation=="SELECTION":
            # select an individual from the generation and add it to the next generation
            add_individual_to_generation(next_generation, select_with_probability(generation, evaluated_values))

        elif selected_operation=="CROSSOVER":
            # select two individuals from the generation
            individual1 = select_with_probability(generation, evaluated_values)
            individual2 = select_with_probability(generation, evaluated_values)
            # select a random index
            index = random.randint(0, len(individual1)-1)
            # create a new individual by combining the two individuals
            new_individual = individual1[:index] + individual2[index:]
            # add the new individual to the next generation
            add_individual_to_generation(next_generation, new_individual)

        else:
            # select an individual from the generation
            individual = select_with_probability(generation, evaluated_values)
            # mutate the individual
            mutated_individual = mutate(individual)
            # add the mutated individual to the next generation
            add_individual_to_generation(next_generation, mutated_individual)

    # update the current generation
    generation = next_generation

# print final generation
print_generation(generation)

# print the strongest individual in the final generation
strongest_individual = generation[evaluate_generation(generation).index(max(evaluate_generation(generation)))]
print("Strongest individual: ")
print_individual(strongest_individual)