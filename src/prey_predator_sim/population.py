from .species import Creature
import matplotlib.pyplot as plt

class Population:

    _instances: set[Creature]

    def __init__(self, n: int, **kwargs):

        self._instances = set(
            [Creature(**kwargs) for _ in range(n)]
        )

        self.history = [n]

    def natural_selection(self):

        for creature in self._instances:
            creature.kill()

        self._instances = set([creature for creature in self._instances if creature.alive])

        self.history.append(self.n)

    @property
    def n(self):
        return len(self._instances)

    def plot_history(self, label="Species"):
        plt.plot(self.history, label=label)
        plt.xlabel("Generation")
        plt.ylabel("Population Size")
        plt.legend()
        plt.show()

    def plot_histogram(self, attr):
        values = [getattr(c, attr) for c in self._instances]

        plt.hist(values, edgecolor="royalblue")
        plt.xlabel(attr)
        plt.ylabel("Number of Creatures")
        plt.show()
