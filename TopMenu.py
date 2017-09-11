from tkinter import *
import MainGui
class TopMenu(Frame):

    def __init__(self):
        self.startGame = 0
        self.__topGui = Tk()
        Frame.__init__(self)
        self.master.title("Menu")
        self.__startButton = Button(self.__topGui, text = "Start Game",
                                    command = self.__runGame)
        self.__quitButton = Button(self.__topGui, text = "Quit",
                                    command = self.master.destroy)
        self.__startButton.pack()
        self.__quitButton.pack()

    def __runGame(self):
        self.startGame = 1
        self.master.destroy()

