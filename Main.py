import random

import simpy
import statistics


def probability(chance):
    return random.random() < chance / 100


class Partner(object):
    def __init__(self):
        self.ayzeh = 10
        self.badyeh = 10
        self.worth = random.random()
        self.mawada = 1
        self.chaos = 1
        self.value = (self.mawada / self.worth) * self.ayzeh * self.chaos

    def BreakUp(self):
        if self.value >= self.ayzeh:
            return False
        else:
            return True


env = simpy.Environment()


class Relationship(object):
    def __init__(self, env, partnera, partnerb):
        self.env = env
        self.partnera = partnera
        self.partnerb = partnerb


Partners = [Partner() for _ in range(2000000)]
print(Partners[60].value)
Relationships = []
for i in range(0, 1000000, 2):
    Relationships.append([Relationship(env=env, partnera=Partners[i], partnerb=Partners[i + 1])])

print(Relationships[30][0].partnerb.value)
print(Relationships[30][0].partnera.value)
