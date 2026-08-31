import random

# Fitness function
def fitness(x):
    return x * x

# Initial population
population = [random.randint(0,10) for i in range(6)]

for generation in range(10):

    # Sort according to fitness
    population.sort(key=fitness, reverse=True)

    # Select best 3
    parents = population[:3]

    # Create new population
    population = parents[:]

    while len(population) < 6:
        parent = random.choice(parents)

        # Mutation
        child = parent + random.choice([-1,0,1])

        # Keep value in range
        child = max(0, min(10, child))

        population.append(child)

best = max(population, key=fitness)

print("Best Value:", best)
print("Maximum Fitness:", fitness(best))
