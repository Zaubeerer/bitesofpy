from typing import Sequence


class Animal:

    sequence = 10000
    zoo_list = []

    def __init__(self, name):
        self.name = name
        self.sequence = Animal.sequence
        Animal.sequence += 1
        Animal.zoo_list.append(str(self))

    def __str__(self):
        return f"{Animal.sequence}. {(self.name).title()}"

    @classmethod
    def zoo(cls):
        return '\n'.join(Animal.zoo_list)
        