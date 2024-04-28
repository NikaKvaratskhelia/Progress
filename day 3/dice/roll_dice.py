import random


class dice:
    def roll():
       x = random.randint(1, 6)
       y = random.randint(1, 6)
       return x, y
