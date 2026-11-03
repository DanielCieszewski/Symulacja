"""Module with definitions of considered species"""
import random

class Creature:

    alive: bool = True

    def __init__(self, p_death: float, p_reproduce: float):
        self.p_death = p_death
        self.p_reproduce = p_reproduce

    def kill(self):
        """Kills (i.e. alive=False) the creature with probability p_death"""
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        """Returns new instance of Creature with probability p_reproduce (otherwise None)"""

        if self.alive and (random.random() < self.p_reproduce):

            # 1. Consider changing p_death, p_reproduce to have instances different from the parent
            # 2. TODO: Change creature class to different one.
            return Creature(p_death=self.p_death, p_reproduce=self.p_reproduce)

        return Noneg