import random
import simpy
import statistics
from matplotlib import pyplot as plt

date = 0


def probability(chance):
    return random.random() < chance / 100


class Partner(object):
    def __init__(self):
        self.ayzeh = 10
        self.badyeh = 10
        self.worth = random.random()
        self.mawada = 1
        self.chaos = 1
        self.value = (self.mawada / self.worth) * self.ayzeh


env = simpy.Environment()


class Relationship(object):
    def __init__(self, env, partnera, partnerb):
        self.env = env
        self.partnera = partnera
        self.partnerb = partnerb

    def breakup(self):
        if self.partnerb.value >= self.partnerb.ayzeh and self.partnera.value >= self.partnera.ayzeh:
            return False
        else:
            return True


Partners = [Partner() for _ in range(200000)]
print(Partners[60].value)
Relationships = []
for i in range(0, 200000, 2):
    Relationships.append([Relationship(env=env, partnera=Partners[i], partnerb=Partners[i + 1])])

print(Relationships[30][0].partnerb.value)
print(Relationships[30][0].partnera.value)


def increasemawada(relation):
    if probability(10):
        relation[0].partnera.mawada += 0.5
    elif probability(10):
        relation[0].partnera.mawada += 0.01
    else:
        relation[0].partnera.mawada += 0.05
    if probability(10):
        relation[0].partnerb.mawada += 0.5
    elif probability(10):
        relation[0].partnerb.mawada += 0.01
    else:
        relation[0].partnerb.mawada += 0.05


def selfworthchange(relation):
    if probability(50):
        relation[0].partnera.worth = random.random()
    if probability(50):
        relation[0].partnerb.worth = random.random()


def ayzehchange(relation):  ##ugly af mekassl afaker
    if relation[0].partnera.ayzeh >= 1:
        if probability(10):
            if probability(50):
                relation[0].partnera.ayzeh += 3
            else:
                relation[0].partnera.ayzeh -= 3
        elif probability(30):
            if probability(50):
                relation[0].partnera.ayzeh += 2
            else:
                relation[0].partnera.ayzeh -= 2
        elif probability(50):
            if probability(50):
                relation[0].partnera.ayzeh += 1
            else:
                relation[0].partnera.ayzeh -= 1
    if relation[0].partnerb.ayzeh >= 1:
        if probability(10):
            if probability(50):
                relation[0].partnerb.ayzeh += 3
            else:
                relation[0].partnerb.ayzeh -= 3
        elif probability(30):
            if probability(50):
                relation[0].partnerb.ayzeh += 2
            else:
                relation[0].partnerb.ayzeh -= 2
        elif probability(50):
            if probability(50):
                relation[0].partnerb.ayzeh += 1
            else:
                relation[0].partnerb.ayzeh -= 1


def badyehchange(relation):
    if relation[0].partnera.badyeh >= 1:
        if probability(10):
            if probability(50):
                relation[0].partnera.badyeh += 3
            else:
                relation[0].partnera.badyeh -= 3
        elif probability(30):
            if probability(50):
                relation[0].partnera.badyeh += 2
            else:
                relation[0].partnera.badyeh -= 2
        elif probability(50):
            if probability(50):
                relation[0].partnera.badyeh += 1
            else:
                relation[0].partnera.badyeh -= 1
    if relation[0].partnerb.badyeh >= 1:
        if probability(10):
            if probability(50):
                relation[0].partnerb.badyeh += 3
            else:
                relation[0].partnerb.badyeh -= 3
        elif probability(30):
            if probability(50):
                relation[0].partnerb.badyeh += 2
            else:
                relation[0].partnerb.badyeh -= 2
        elif probability(50):
            if probability(50):
                relation[0].partnerb.badyeh += 1
            else:
                relation[0].partnerb.badyeh -= 1


sumworth = 0
summawada = 0
sumayzeh = 0
sumbadyeh = 0
graph = []
while date != 120:
    date += 1
    for relation in Relationships:
        increasemawada(relation)
        selfworthchange(relation)
        ayzehchange(relation)
        badyehchange(relation)
        relation[0].partnera.chaos = random.randint(-2, 3)
        relation[0].partnerb.chaos = random.randint(-2, 3)
        relation[0].partnera.value = (relation[0].partnera.mawada / relation[0].partnera.worth) * relation[
            0].partnera.ayzeh
        relation[0].partnerb.value = (relation[0].partnerb.mawada / relation[0].partnerb.worth) * relation[
            0].partnerb.ayzeh
        if relation[0].breakup():
            Relationships.remove(relation)  # del relation didn't work msh 3arf leh
    graph.append(len(Relationships))
for relation in Relationships:
    sumworth += relation[0].partnera.worth + relation[0].partnerb.worth
    summawada += relation[0].partnera.mawada + relation[0].partnerb.mawada
    sumayzeh += relation[0].partnera.ayzeh + relation[0].partnerb.ayzeh
    sumbadyeh += relation[0].partnera.badyeh + relation[0].partnerb.badyeh
print(summawada / (len(Relationships) * 2))
print(sumworth / (len(Relationships) * 2))
print(sumayzeh / (len(Relationships) * 2))
print(sumbadyeh / (len(Relationships) * 2))
plt.plot(graph)
plt.show()
