from tkinter import *
from abc import ABC, abstractmethod


#class AbstractView(ABC):    

class View():

    def __init__(self):
        """
        Creates a view with the defined characteristics.
        """

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

 
        root.mainloop() # Starts/runs the GUI (everything involving the GUI should come before this)
    def tileChoiceChange(self):    
        print(f'{self.var1.get()} {self.var2.get()} {self.var3.get()} {self.var4.get()} {self.var5.get()} {self.var6.get()} {self.var7.get()} {self.var8.get()} {self.var9.get()}')
