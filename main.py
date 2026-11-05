from src.prey_predator_sim.population import Population

population = Population(
    n=100,
    p_death=0.2,
    p_reproduce=0.3
)

print("Initial population:", population.n)

for generation in range(10):
    population.natural_selection()
    print(f"Generation {generation + 1}: {population.n}")

population.plot_history()