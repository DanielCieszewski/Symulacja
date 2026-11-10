import random

random.seed(489)

from src.prey_predator_sim.species import Prey, Predator
from src.prey_predator_sim.population import Population

population = Population(
    population_data={
        Prey: 30,
        Predator: 30
    },
    species_parameters={
        Prey: {
            "p_death": 0.5,
            "p_reproduce": 0.5,
            "p_hunt": 0.5
        },
        Predator: {
            "p_death": 0.5,
            "p_reproduce": 0.5
        }
    }
)

for _ in range(12):
    population.natural_selection()

population.plot_history()