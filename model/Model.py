from abc import ABC, abstractmethod
import random   # For the dice rolls

#class AbstractModel(ABC):


class Model():

    def rollDice(self):
        roll = random.randint(1, 6) # A six-sided dice
        return roll


    def sumBinaryList(self, binary_list):
        """
        Iterates through the list of binary.
        If the value at an entry is 1, then adds the index value to total sum.
        Returns the sum of the list and the tiles that were added.
        """
        binary_sum = 0
        tile_list = []

        for index in range(9):  # There will only ever be 9 tiles, so the range can be hard-coded
            if binary_list[index] == 1:
                binary_sum += (index + 1)   # (index + 1) represents the tile number
                tile_list.append(index + 1)

        return binary_sum, tile_list


    def determineScore(self, tile_values):
        """
        From the tiles left uncovered, determines and returns the player's score.
        """
        score = 0

        # Go through each tile state and, if not negative, add index to score
        for index in range(9):
            if tile_values[index] != -1:
                score += (index + 1)

        return score


