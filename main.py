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
        steps: int = 150,
        plot: bool = False
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

    if plot:
        population.plot_history()

    return population.history



def run_experiment(
        repetitions: int,
        n_prey: int,
        n_predator: int,
        prey_p_death: float,
        prey_p_reproduce: float,
        prey_p_hunt: float,
        predator_p_death: float,
        predator_p_reproduce: float,
        steps: int = 150,
        seed_start: int = 0,
        plot: bool = False
):
    results = []

    for i in range(repetitions):
        history = run_simulation(
            seed=seed_start + i,
            n_prey=n_prey,
            n_predator=n_predator,
            prey_p_death=prey_p_death,
            prey_p_reproduce=prey_p_reproduce,
            prey_p_hunt=prey_p_hunt,
            predator_p_death=predator_p_death,
            predator_p_reproduce=predator_p_reproduce,
            steps=steps,
            plot=plot
        )

        results.append(history[-1])

    prey_final = [result[Prey] for result in results]
    predator_final = [result[Predator] for result in results]
    total_final = [
        prey_final[i] + predator_final[i]
        for i in range(repetitions)
    ]

    print(f"\nResults after {repetitions} simulations ({steps} steps)")
    print(f"Prey extinction: {sum(x == 0 for x in prey_final) / repetitions * 100:.2f}%")
    print(f"Predator extinction: {sum(x == 0 for x in predator_final) / repetitions * 100:.2f}%")
    print(f"Final population mean: {statistics.mean(total_final):.2f}")
    print(f"Final population standard deviation: {statistics.stdev(total_final):.2f}")

    return results



results = run_experiment(
    repetitions=10,
    n_prey=30,
    n_predator=30,
    prey_p_death=0.01,
    prey_p_reproduce=0.4,
    prey_p_hunt=0.5,
    predator_p_death=0.99,
    predator_p_reproduce=0.99,
    steps=15,
    seed_start=4771,
)