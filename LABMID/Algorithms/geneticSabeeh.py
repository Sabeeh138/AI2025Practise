import random

# Fitness function: counts non-attacking pairs of queens
def calculate_fitness(individual, n):
    non_attacking_pairs = 0
    total_pairs = n * (n - 1) // 2  # Maximum possible non-attacking pairs

    for i in range(n):
        for j in range(i + 1, n):
            # No same column or diagonal conflict
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1

    return non_attacking_pairs / total_pairs  # Fitness score as a ratio

# Generate a random individual (chromosome) based on column positions
def create_random_individual(n):
    return random.sample(range(n), n)  # Ensure unique column positions

# Select the best routes (parents) based on fitness
def select_parents(population, fitness_scores):
    sorted_population = [board for _, board in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:len(population)//2]

# Crossover function: single-point crossover with unique column
def crossover(parent1, parent2, n):
    point = random.randint(1, n - 2)  # Choose a crossover point
    child = parent1[:point] + parent2[point:]

    # Ensure unique column positions
    missing = set(range(n)) - set(child)
    duplicates = [col for col in child if child.count(col) > 1]
    for i in range(len(child)):
        if child.count(child[i]) > 1:
            child[i] = missing.pop()
    return child

# Mutation function: randomly swap two positions
def mutate(individual, n):
    idx1, idx2 = random.sample(range(n), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Genetic Algorithm main function
def genetic_algorithm(n, population_size=10, mutation_rate=0.1, max_generations=100):
    population = [create_random_individual(n) for _ in range(population_size)]
    generation = 0
    best_fitness = 0

    while best_fitness < 1.0 and generation < max_generations:
        fitness_scores = [calculate_fitness(ind, n) for ind in population]
        best_fitness = max(fitness_scores)
        print(f"Generation {generation} Best Fitness: {best_fitness}")

        if best_fitness == 1.0:
            break

        parents = select_parents(population, fitness_scores)
        new_population = [crossover(random.choice(parents), random.choice(parents), n) for _ in range(population_size)]

        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i], n)

        population = new_population
        generation += 1

    best_individual = max(population, key=lambda ind: calculate_fitness(ind, n))
    return best_individual, calculate_fitness(best_individual, n)

# Run the Genetic Algorithm for 8-Queens problem
n = 8  # Change N for different problem sizes
solution, fitness = genetic_algorithm(n)

print("Best Solution:", solution)
print("Best Fitness:", fitness)
