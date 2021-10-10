import random

import simpy
import statistics


def probability(chance):
    return random.random() < chance / 100


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


class Relationship(object):
    def __init__(self, partnera, partnerb, env):
        self.env = env
        self.partnera = partnera
        self.partnerb = partnerb
