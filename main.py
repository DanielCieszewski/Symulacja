from src.prey_predator_sim.species import Prey, Predator
from src.prey_predator_sim.population import Population

population = Population(
    population_data={
        Prey: 30,
        Predator: 30
    },
    species_parameters={
        Prey: {
            "p_death": 0.02,
            "p_reproduce": 0.4,
            "p_hunt": 0.327
        },
        Predator: {
            "p_death": 0.02,
            "p_reproduce": 0.4
        }
    }
)

for _ in range(20):
    population.natural_selection()

population.plot_history()