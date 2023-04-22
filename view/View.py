from tkinter import *
from abc import ABC, abstractmethod
from controller.Controller import Controller


#class AbstractView(ABC):    

class View():

    def __init__(self, controller: Controller):
        """
        Creates a view with the defined characteristics.
        """

        # Initializing the root window
        self.root = Tk()
        self.root.geometry("600x400")    # Dimensions of the frame (window)
        self.root.title("Shut the Box")  # Used to add a title to the whole window

        # Initializing variables
        self.controller = controller
        self.dice_results = 0  
        self.tile_states = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]  # List for holding the state of the tiles 
        self.active_tiles = []  # A list of the tiles currently selected by the player

        # Top of root window
        self.topframe = Frame(self.root, height=200, width=300, bg="#331a00")  # 'root' refers to the parent frame that this frame is inside. Root is the main window.
        self.topframe.pack(expand=True, fill=BOTH)
    
        # Tiles
        self.tile1 = Checkbutton(self.topframe, text="1", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[0], state=DISABLED)
        self.tile1.place(relx=0.01, rely=0.3)

        self.tile2 = Checkbutton(self.topframe, text="2", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[1], state=DISABLED)
        self.tile2.place(relx=0.12, rely=0.3)

        self.tile3 = Checkbutton(self.topframe, text="3", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[2], state=DISABLED)
        self.tile3.place(relx=0.23, rely=0.3)

        self.tile4 = Checkbutton(self.topframe, text="4", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[3], state=DISABLED)
        self.tile4.place(relx=0.34, rely=0.3)

        self.tile5 = Checkbutton(self.topframe, text="5", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[4], state=DISABLED)
        self.tile5.place(relx=0.45, rely=0.3)

        self.tile6 = Checkbutton(self.topframe, text="6", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[5], state=DISABLED)
        self.tile6.place(relx=0.56, rely=0.3)

        self.tile7 = Checkbutton(self.topframe, text="7", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[6], state=DISABLED)
        self.tile7.place(relx=0.67, rely=0.3)

        self.tile8 = Checkbutton(self.topframe, text="8", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[7], state=DISABLED)
        self.tile8.place(relx=0.78, rely=0.3)

        self.tile9 = Checkbutton(self.topframe, text="9", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.tile_states[8], state=DISABLED)
        self.tile9.place(relx=0.89, rely=0.3)


        # Bottom of root window
        self.bottomframe = Frame(self.root, height=200, width=300, bg="#004d00")
        self.bottomframe.pack(expand=True, fill=BOTH)

        # Dice roll 1 button
        self.diceroll1_button = Button(self.bottomframe, height=2, width=10, bg="black", fg="gray", activebackground="#1a1a1a", activeforeground="gray", text="Roll One Dice", font=("Arial", 10, "italic"), command=self.generateRoll1)
        self.diceroll1_button.place(relx=0.1, rely=0.15)

        # Dice roll 2 button
        self.diceroll2_button = Button(self.bottomframe, height=2, width=10, bg="black", fg="gray", activebackground="#1a1a1a", activeforeground="gray", text="Roll Two Dice", font=("Arial", 10, "italic"), command=self.generateRoll2)
        self.diceroll2_button.place(relx=0.7, rely=0.15)

        # Cover tiles button
        self.covertiles_button = Button(self.bottomframe, height=2, width=10, bg="#004d00", fg="white", activebackground="#800000", activeforeground="black", text="Cover Tiles", font=("Arial", 10, "italic"), state=DISABLED, command=self.coverTiles)
        self.covertiles_button.place(relx=0.39, rely=0.6)

        # Dice results
        diceresults = Frame(self.bottomframe, height=73, width=73, bg="#003300")
        diceresults.place(relx=0.43, rely=0.1)
        self.dicelabel = Label(diceresults, text="", fg="white", bg="#003300", font=("Arial", 16, "bold"))
        self.dicelabel.place(relx=0.3, rely=0.3)

        # End game button
        self.endgame_button = Button(self.bottomframe, height=1, width=6, bg="#cc7a00", fg="black", text="End Game", command=self.endGame)
        self.endgame_button.place(relx=0.87, rely=0.86)

        self.root.mainloop() # Starts/runs the GUI (everything involving the GUI should come before this)


    def tileChoiceChange(self):
        """
        Every time a new tile is checked by the user, this method will request a sum
        of the currently-checked tiles from the model to be compared with the dice roll.
        Enables the cover tile button if the two values are equal.
        """
        binary_state_list = []

        # Populate the list of current tile states
        for val in range(9):
            binary_state_list.append(self.tile_states[val].get())

        # Send list to controller to request sum from model
        tile_sum, self.active_tiles = self.controller.getBinaryListSum(binary_state_list)            

        # Check if player is allowed to cover the current tiles
        self.canCoverTiles(tile_sum)


    def canCoverTiles(self, sum_of_tiles):
        """
        Given the current state of tiles selected, will determine if player is
        allowed to cover the tiles and, if so, enable the cover tile button
        """
        # Checking if the selected tiles is equal to the dice roll
        if sum_of_tiles == self.dice_results:
            self.covertiles_button['state'] = NORMAL    # enabling the cover tiles button
            self.covertiles_button['bg'] = "#660000"
            self.covertiles_button['fg'] = "white"
            self.covertiles_button['activeforeground'] = "white"
        else:
            self.covertiles_button['state'] = DISABLED  # disabling the cover tiles button
            self.covertiles_button['bg'] = "#004d00"
            self.covertiles_button['fg'] = "gray"



    def postRollGameState(self):
        """
        Called after rolling the dice the disable dice roll buttons and show tile values.
        Can't have the user rolling twice because they didn't like their roll now can we?
        """
        # Disabling the dice roll buttons
        self.diceroll1_button['state'] = DISABLED
        self.diceroll2_button['state'] = DISABLED
        self.diceroll1_button['bg'] = "#004d00"
        self.diceroll2_button['bg'] = "#004d00"

        # Enable the tiles for selecting if they haven't already been covered
        if self.tile1['bg'] != "#331a00":
            self.tile1['state'] = NORMAL
        if self.tile2['bg'] != "#331a00":
            self.tile2['state'] = NORMAL
        if self.tile3['bg'] != "#331a00":
            self.tile3['state'] = NORMAL
        if self.tile4['bg'] != "#331a00":
            self.tile4['state'] = NORMAL
        if self.tile5['bg'] != "#331a00":
            self.tile5['state'] = NORMAL
        if self.tile6['bg'] != "#331a00":
            self.tile6['state'] = NORMAL
        if self.tile7['bg'] != "#331a00":
            self.tile7['state'] = NORMAL
        if self.tile8['bg'] != "#331a00":
            self.tile8['state'] = NORMAL
        if self.tile9['bg'] != "#331a00":
            self.tile9['state'] = NORMAL


    def generateRoll1(self):
        """
        Send a request to the controller to roll one dice
        """
        roll_result = self.controller.requestRoll(1)    # requesting 1 dice roll
        self.dice_results = roll_result
        self.dicelabel['text'] = str(roll_result)

        self.postRollGameState()


    def generateRoll2(self):
        """
        Sends a request to the controller to roll two dice
        """
        roll_result = self.controller.requestRoll(2)    # requesting 2 dice rolls
        self.dice_results = roll_result
        self.dicelabel['text'] = str(roll_result)

        self.postRollGameState()


    def coverTiles(self):
        """
        Covers the requested tiles and refresh the game loop to the dice roll state
        """
        # Cover the currently selected tiles
        for tile in self.active_tiles:
            if tile == 1:
                self.tile1['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
            elif tile == 2:    
                self.tile2['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
            elif tile == 3:    
                self.tile3['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
            elif tile == 4:    
                self.tile4['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
            elif tile == 5:    
                self.tile5['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
            elif tile == 6:    
                self.tile6['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
            elif tile == 7:    
                self.tile7['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
            elif tile == 8:    
                self.tile8['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
            elif tile == 9:    
                self.tile9['bg'] = "#331a00"
                self.tile_states[tile-1].set(-1)
        
        # Disable the tiles for the start of the next game loop
        self.disableTiles()

        
    def disableTiles(self):
        """
        Puts all of the tiles into a disabled state
        """
        self.tile1['state'] = DISABLED
        self.tile2['state'] = DISABLED
        self.tile3['state'] = DISABLED
        self.tile4['state'] = DISABLED
        self.tile5['state'] = DISABLED
        self.tile6['state'] = DISABLED
        self.tile7['state'] = DISABLED
        self.tile8['state'] = DISABLED
        self.tile9['state'] = DISABLED

        # Prepare box for next round of game
        self.roundPrep()


    def roundPrep(self):
        """
        Prepares the box for the next dice roll by disabling/enabling required
        buttons and clearing the old dice roll.
        """
        # Disable cover tile button
        self.covertiles_button['bg'] = "#004d00"
        self.covertiles_button['state'] = DISABLED
        

        # Enable the dice roll buttons
        self.diceroll1_button['bg'] = "black"
        self.diceroll1_button['state'] = NORMAL
        self.diceroll2_button['bg'] = "black"
        self.diceroll2_button['state'] = NORMAL

        # Clear the old dice roll
        self.dicelabel['text'] = ""


    def endGame(self):
        """
        Requests the controller to calculate the end score and terminates the game.
        """
        state_values = []

        # Populate state_values with current states
        for tile in self.tile_states:
            state_values.append(tile.get())

        score = self.controller.calculateScore(state_values)
        self.scoreScreen(score)


    def scoreScreen(self, score):
        """
        Clears the window and displays the score
        """
        # Clear the game window
        self.topframe.destroy()
        self.bottomframe.destroy()

        # Display the score
        score_message = f'Score: {score}'

        endframe = Frame(self.root, height=400, width=600, bg="#999966")  # 'root' refers to the parent frame that this frame is inside. Root is the main window.
        endframe.pack(expand=True, fill=BOTH)
        scorelabel = Label(endframe, text=score_message, font=("Comic Sans", 36, "bold"), bg="#999966")
        scorelabel.place(relx=0.28, rely=0.2)

        # Exit button
        exitbutton = Button(endframe, command=self.terminate, text="EXIT", font=("Comic Sans", 20), bg="black", fg="white", height=2, width=4, activebackground="#1a1a1a", activeforeground="white")
        exitbutton.place(relx=0.42, rely=0.6)


    def terminate(self):
        """
        Terminates the game completely.
        """
        self.root.quit()




