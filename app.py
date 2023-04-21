# from model import Model 
from view.View import View
# from controller import Controller


class App:
    def __init__(self):

        # create a view and place it on the root window
        self.view = View()


if __name__ == '__main__':
    app = App()
