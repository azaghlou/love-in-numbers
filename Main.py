import random

import simpy
import statistics


class Partners(object):
    def __init__(self):
        self.ayzeh = 10
        self.badyeh = 10
        self.worth = random.random()
        self.mawada = 1
        self.value = (self.mawada / self.worth) * self.ayzeh

    def BreakUp(self):
        if self.value >= self.ayzeh:
            return False
        else:
            return True
