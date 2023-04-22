from abc import ABC, abstractmethod


class AbstractModel(ABC):

    @abstractmethod
    def rollDice(self):
        """
        Returns a random number between 1 and 6 to simulate a dice roll.
        """
        pass


    @abstractmethod
    def sumBinaryList(self, binary_list):
        """
        Iterates through the list of binary.
        If the value at an entry is 1, then adds the index value to total sum.
        Returns the sum of the list and the tiles that were added.
        """
        pass


    @abstractmethod
    def determineScore(self, tile_values):
        """
        From the tiles left uncovered, determines and returns the player's score.
        """
        pass

