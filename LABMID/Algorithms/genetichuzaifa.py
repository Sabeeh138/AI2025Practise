import random

MAX_GENS = 100
Mutation_rate = 0.2
Population_size = 20 

Target = [5, 8, 2, 6, 9]

def Generate_Random_List():
    return [random.randint(1, 9) for _ in range(5)]

def Fitness_Score(individual):
    return sum(1 for i in range(len(Target)) if individual[i] == Target[i])

def Select_Parents(population):
    return sorted(population, key=Fitness_Score, reverse=True)[:2]

def Cross_over(Parent1, Parent2):
    index = random.randint(1, len(Parent1) - 2)
    return Parent1[:index] + Parent2[index:]

def Mutation(individual):
    if random.random() < Mutation_rate:
        index = random.randint(0, len(Target) - 1)
        individual[index] = random.randint(1, 9)
    if random.random() < Mutation_rate:
        index = random.randint(0, len(Target) - 1)
        individual[index] = random.randint(1, 9)
    return individual

population = [Generate_Random_List() for _ in range(Population_size)]

for generation in range(MAX_GENS):
    fitness = [Fitness_Score(ind) for ind in population]
    best_fitness = max(fitness)  

    print(f"Generation {generation + 1},  Best Fitness: {best_fitness}")

    if best_fitness == len(Target):
        break

    parents = Select_Parents(population)

    new_population = [Cross_over(parents[0], parents[1]) for _ in range(Population_size - 2)]
    new_population = [Mutation(child) for child in new_population]

    population = parents + new_population
    
best_solution = max(population, key=Fitness_Score)
print("\n Best Solution Found:", best_solution)
print(" Best Fitness Score:", Fitness_Score(best_solution))