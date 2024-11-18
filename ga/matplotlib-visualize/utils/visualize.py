import matplotlib.pyplot as plt

def visualize_generation(fitness_scores):
    """ This function visualizes the fitness evolution over generations
    """
    plt.plot([i for i in range(len(fitness_scores))], fitness_scores, marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Fitness Score')
    plt.title('Fitness Evolution Over Generations')
    plt.show()
