import random

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

def apply_operation(operations, operation_probabilities, generation, evaluated_values, next_generation):
    """ This function applies an operation to the generation
    """
    selected_operation=select_with_probability(operations, operation_probabilities)
    print("Selected operation: ",selected_operation)

    if selected_operation=="SELECTION":
        add_individual_to_generation(next_generation, select_with_probability(generation, evaluated_values))

    elif selected_operation=="CROSSOVER":
        individual1 = select_with_probability(generation, evaluated_values)
        individual2 = select_with_probability(generation, evaluated_values)

        index = random.randint(0, len(individual1)-1)
        # create a new individual by combining the two individuals
        new_individual = individual1[:index] + individual2[index:]
        add_individual_to_generation(next_generation, new_individual)

    else: # selected_operation=="MUTATION"
        individual = select_with_probability(generation, evaluated_values)
        # mutate the individual
        mutated_individual = mutate(individual)
        add_individual_to_generation(next_generation, mutated_individual)

def create_next_generation(generation, operations, operation_probabilities):
    """ This function creates the next generation from the current generation
    """

    # create a next generation from the current generation
    next_generation = []
    for i in range(len(generation)):
        evaluated_values = evaluate_generation(generation)
        apply_operation(operations, operation_probabilities, generation, evaluated_values, next_generation)
    return next_generation

def genetic_algorithm(generation, num_of_generation, operations, operation_probabilities):
    """ This function runs the genetic algorithm
    """

    fitness_scores = []
    fitness_scores.append(max(evaluate_generation(generation)))

    # create a next generation from the current generation
    for i in range(num_of_generation):
        print_generation(generation)

        # create a next generation from the current generation
        generation=create_next_generation(generation, operations, operation_probabilities)
        fitness_scores.append(max(evaluate_generation(generation)))

    # print final generation
    print_generation(generation)

    # print the strongest individual in the final generation
    strongest_individual = generation[evaluate_generation(generation).index(max(evaluate_generation(generation)))]
    print("Strongest individual: ")
    print_individual(strongest_individual)

    return fitness_scores
