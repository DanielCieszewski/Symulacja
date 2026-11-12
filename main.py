from src.prey_predator_sim.population import Population
from src.prey_predator_sim.species import Prey, Predator
import random
import statistics

def run_simulation(
        seed: int,
        n_prey: int,
        n_predator: int,
        prey_p_death: float,
        prey_p_reproduce: float,
        prey_p_hunt: float,
        predator_p_death: float,
        predator_p_reproduce: float,
        steps: int = 150
):
    random.seed(seed)

    population = Population(
        population_data={
            Prey: n_prey,
            Predator: n_predator
        },
        species_parameters={
            Prey: {
                "p_death": prey_p_death,
                "p_reproduce": prey_p_reproduce,
                "p_hunt": prey_p_hunt
            },
            Predator: {
                "p_death": predator_p_death,
                "p_reproduce": predator_p_reproduce
            }
        }
    )

    for _ in range(steps):
        population.natural_selection()

    population.plot_history()

    return population.history



history = run_simulation(
    seed=55,
    n_prey=30,
    n_predator=30,
    prey_p_death=0.9,
    prey_p_reproduce=0.9,
    prey_p_hunt=0.5,
    predator_p_death=0.9,
    predator_p_reproduce=0.9
)