from tkinter import *
import sys


class GameOver(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.top = Tk()
        self.gameOver = Label(self.top,
        text = "You failed to discover the truth and were"\
                " destroyed by your inner demons.")
        self.gameQuit = Button(self.top, text = "OK",
                                command = self.top.destroy)
        self.gameOver.pack()
        self.gameQuit.pack()
    
