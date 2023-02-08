import random


class Insect:
    def __init__(self):
        self.legs = 4
        self.wings = 2
        self.length = 10

    def flight(self):
        self.length = random.randint(1, 10)

    def get_length(self):
        return self.length
