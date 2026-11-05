from src.prey_predator_sim.population import Population

population = Population(
    n=30,
    p_death=0.01,
    p_reproduce=0.01001
)

print("Initial population:", population.n)

for generation in range(100):
    population.natural_selection()
    print(f"Generation {generation + 1}: {population.n}")

population.plot_history()