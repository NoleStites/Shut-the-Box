from tkinter import *
from abc import ABC, abstractmethod
from controller.Controller import Controller


#class AbstractView(ABC):    

class View():

    def __init__(self, controller: Controller):
        """
        Creates a view with the defined characteristics.
        """

        # Getting the controller
        self.controller = controller

        # Initializing the root window
        root = Tk()
        root.geometry("600x400")    # Dimensions of the frame (window)
        root.title("Shut the Box")  # Used to add a title to the whole window
        
        # Intialize tile-state variables
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()

        # Top of root window
        topframe = Frame(root, height=200, width=300, bg="#331a00")  # 'root' refers to the parent frame that this frame is inside. Root is the main window.
        topframe.pack(expand=True, fill=BOTH)
    
        # Tiles
        tile1 = Checkbutton(topframe, text="1", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var1)
        tile1.place(relx=0.01, rely=0.3)

        tile2 = Checkbutton(topframe, text="2", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var2)
        tile2.place(relx=0.12, rely=0.3)

        tile3 = Checkbutton(topframe, text="3", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var3)
        tile3.place(relx=0.23, rely=0.3)

        tile4 = Checkbutton(topframe, text="4", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var4)
        tile4.place(relx=0.34, rely=0.3)

        tile5 = Checkbutton(topframe, text="5", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var5)
        tile5.place(relx=0.45, rely=0.3)

        tile6 = Checkbutton(topframe, text="6", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var6)
        tile6.place(relx=0.56, rely=0.3)

        tile7 = Checkbutton(topframe, text="7", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var7)
        tile7.place(relx=0.67, rely=0.3)

        tile8 = Checkbutton(topframe, text="8", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var8)
        tile8.place(relx=0.78, rely=0.3)

        tile9 = Checkbutton(topframe, text="9", height=3, width=1, bg="#a6a6a6", activebackground="#bfbfbf", fg="black", font=("Arial", 16, "bold"), relief=RAISED, command=self.tileChoiceChange, variable=self.var9)
        tile9.place(relx=0.89, rely=0.3)


        # Bottom of root window
        bottomframe = Frame(root, height=200, width=300, bg="#004d00")
        bottomframe.pack(expand=True, fill=BOTH)

        # Dice roll 1 button
        self.diceroll1_button = Button(bottomframe, height=2, width=10, bg="black", fg="gray", activebackground="#1a1a1a", activeforeground="gray", text="Roll One Dice", font=("Arial", 10, "italic"), command=self.generateRoll1)
        self.diceroll1_button.place(relx=0.1, rely=0.15)

        # Dice roll 2 button
        self.diceroll2_button = Button(bottomframe, height=2, width=10, bg="black", fg="gray", activebackground="#1a1a1a", activeforeground="gray", text="Roll Two Dice", font=("Arial", 10, "italic"), command=self.generateRoll2)
        self.diceroll2_button.place(relx=0.7, rely=0.15)

        # Cover tiles button
        self.covertiles_button = Button(bottomframe, height=2, width=10, bg="gray", fg="black", activebackground="#999966", activeforeground="black", text="Cover Tiles", font=("Arial", 10, "italic"), state=DISABLED, command=self.coverTiles)
        self.covertiles_button.place(relx=0.39, rely=0.6)

        # Dice results
        diceresults = Frame(bottomframe, height=73, width=73, bg="#003300")
        diceresults.place(relx=0.43, rely=0.1)
        self.dicelabel = Label(diceresults, text="", fg="white", bg="#003300", font=("Arial", 16, "bold"))
        self.dicelabel.place(relx=0.3, rely=0.3)

        root.mainloop() # Starts/runs the GUI (everything involving the GUI should come before this)


    def tileChoiceChange(self):    
        print(f'{self.var1.get()} {self.var2.get()} {self.var3.get()} {self.var4.get()} {self.var5.get()} {self.var6.get()} {self.var7.get()} {self.var8.get()} {self.var9.get()}')


    def generateRoll1(self):
        """
        Send a request to the controller to roll one dice
        Returns value of roll.
        """
        roll_result = self.controller.requestRoll(1)    # requesting 1 dice roll
        self.dicelabel['text'] = str(roll_result)


    def generateRoll2(self):
        """
        Sends a request to the controller to roll two dice
        returns value of roll.
        """
        roll_result = self.controller.requestRoll(2)    # requesting 2 dice rolls
        self.dicelabel['text'] = str(roll_result)


    def coverTiles(self):
        """
        Covers the requested tiles
        """
        pass
