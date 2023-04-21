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
