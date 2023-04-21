from abc import ABC, abstractmethod
import random   # For the dice rolls

#class AbstractModel(ABC):


class Model():

    def rollDice(self):
        roll = random.randint(1, 6) # A six-sided dice
        return roll

