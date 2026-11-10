from dataclasses import dataclass
import matplotlib.pyplot as plt
import random

from .species import Creature, Prey, Predator


class Population:
    _instances: set[Creature]
    history: list[dict]

    def __init__(self, population_data: dict, species_parameters: dict):

        self._instances = set()

        for species, n in population_data.items():
            for _ in range(n):
                creature = species(**species_parameters[species])
                self._instances.add(creature)

        self.history = [self.n]

    def count_species(self, species):
        return sum(
            isinstance(creature, species)
            for creature in self._instances
        )

    def count_population(self, instances):
        return {
            Prey: sum(isinstance(c, Prey) for c in instances),
            Predator: sum(isinstance(c, Predator) for c in instances)
        }

    @property
    def n(self):
        return self.count_population(self._instances)

    def hunting(self):

        prey = [
            c for c in self._instances
            if isinstance(c, Prey) and c.alive
        ]

        predators = [
            c for c in self._instances
            if isinstance(c, Predator) and c.alive
        ]

        random.shuffle(prey)
        random.shuffle(predators)

        for predator, prey_animal in zip(predators, prey):
            predator.hunt(prey_animal)

    def natural_selection(self):

        # 1. Reproduction
        offspring = set()

        for creature in self._instances:
            if creature.alive:
                new_creature = creature.reproduce()

                if new_creature is not None:
                    offspring.add(new_creature)

        # 2. Hunting
        self.hunting()

        # 3. Death
        for creature in self._instances:
            if creature.alive:
                creature.kill()

        # 4. History
        survivors = {
            creature for creature in self._instances
            if creature.alive
        }

        next_population = survivors | offspring

        self.history.append(
            self.count_population(next_population)
        )

        # 5. New population
        self._instances = next_population

    def plot_history(self):

        prey_history = [element[Prey] for element in self.history]
        predator_history = [element[Predator] for element in self.history]

        plt.plot(prey_history, label="Prey", color="#4A412A")
        plt.plot(predator_history, label="Predators", color="blue")

        plt.xlabel("Generation")
        plt.ylabel("Population size")
        plt.title("Population history")
        plt.ylim(bottom=0)
        plt.legend()
        plt.show()

    def plot_histogram(self, attr):

        values = [
            getattr(creature, attr)
            for creature in self._instances
            if hasattr(creature, attr)
        ]

        plt.hist(values, edgecolor="black")
        plt.xlabel(attr)
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {attr}")
        plt.show()
