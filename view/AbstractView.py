from abc import ABC, abstractmethod


class AbstractView(ABC):

    @abstractmethod
    def tileChoiceChange(self):
        """
        Every time a new tile is checked by the user, this method will request a sum
        of the currently-checked tiles from the model to be compared with the dice roll.
        Enables the cover tile button if the two values are equal.
        """
        pass


    @abstractmethod
    def canCoverTiles(self, sum_of_tiles):
        """
        Given the current state of tiles selected, will determine if player is
        allowed to cover the tiles and, if so, enable the cover tile button
        """
        pass


    @abstractmethod
    def postRollGameState(self):
        """
        Called after rolling the dice the disable dice roll buttons and show tile values.
        Can't have the user rolling twice because they didn't like their roll now can we?
        """
        pass


    @abstractmethod
    def generateRoll1(self):
        """
        Send a request to the controller to roll one dice
        """
        pass


    @abstractmethod
    def generateRoll2(self):
        """
        Sends a request to the controller to roll two dice
        """
        pass


    @abstractmethod
    def coverTiles(self):
        """
        Covers the requested tiles and refresh the game loop to the dice roll state
        """
        pass


    @abstractmethod
    def disableTiles(self):
        """
        Puts all of the tiles into a disabled state
        """
        pass


    @abstractmethod
    def roundPrep(self):
        """
        Prepares the box for the next dice roll by disabling/enabling required
        buttons and clearing the old dice roll.
        """
        pass


    @abstractmethod
    def endGame(self):
        """
        Requests the controller to calculate the end score and terminates the game.
        """
        pass


    @abstractmethod
    def scoreScreen(self, score):
        """
        Clears the window and displays the score
        """
        pass


    @abstractmethod
    def terminate(self):
        """
        Terminates the game completely.
        """
        pass
