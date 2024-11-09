import random

class Misc:
    def randompositions(amount, boundaries):
        randompositions = []
        for i in range(0, amount):
            randompositions.append((random.randint(0, boundaries[0]), random.randint(0, boundaries[1])))
        return randompositions