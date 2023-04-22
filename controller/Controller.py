from model.Model import Model

class Controller():

    def __init__(self, model: Model):
        self.model = model


    def requestRoll(self, num_rolls: int):
        """
        Requests the model to roll a number of dice and return the results.
        """

        roll_totals = 0 # Initialize the roll total

        # Rolls dice num_rolls times
        for num in range(num_rolls):
            roll_totals += self.model.rollDice()

        return roll_totals


    def getBinaryListSum(self, binary_list):
        """
        Sends list of binary to model for adding, then returns result to view.
        """
        binary_sum, tile_list = self.model.sumBinaryList(binary_list)
        return binary_sum, tile_list


    def calculateScore(self, tile_values):
        """
        Requests the model to return a score based on the state of the tiles at the end of the game
        """
        score = self.model.determineScore(tile_values)
        return score

