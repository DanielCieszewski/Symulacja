from .species import Creature
import matplotlib.pyplot as plt


class Population:
    _instances: set[Creature]  # wszystkie aktualnie zyjace Creature
    history: list[int]  # historia liczebnosci populacji

    def __init__(self, n: int, **kwargs):

        self._instances = set(
            [Creature(**kwargs) for _ in range(n)]
        )

        self.history = [self.n]

    def natural_selection(self):

        for creature in self._instances:
            creature.kill()

        self._instances = set([creature for creature in self._instances if creature.alive])

        offspring = set()

        for creature in self._instances:
            new_creature = creature.reproduce()

            if new_creature is not None:
                offspring.add(new_creature)

        self._instances.update(offspring)

        self.history.append(self.n)

    def plot_history(self):
        plt.plot(self.history, color="brown")
        plt.xlabel("Generation")
        plt.ylabel("Size")
        plt.title("History")
        plt.ylim(bottom=0)
        plt.show()


    @property
    def n(self):
        return len(self._instances)