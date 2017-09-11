from tkinter import *
from _Speech import *
from MasterProcess import *
import gameOver
import winningScreen

class MainGui(Frame):
    def commandSubmit(self, null):
        self.__turnsLeft -= 1
        if self.__turnsLeft == 0:
            dead = gameOver.GameOver()
            self.master.destroy()
            dead.mainloop()
        self.__turns.set(self.__turnsLeft)
        self.__lines += 2
        userInput = self.__commandLine.get()
        currentOutput = self.__output.get()


        output = str(masterProcess(userInput, self.__currentRoom,
                     self.__inventory))
        try:
            outputCut = output.split("|")
            if outputCut[1] != "":
                self.__inventory.append(outputCut[1])
                invent = ""
                for item in self.__inventory:
                    invent = invent + "\n" + item
                self.__invent.set(invent)
            self.__currentRoom = outputCut[2]
            output = outputCut[0]
            if len(output) < 70:
                pass
            elif len(output) < 140:
                self.__lines += 1
            elif len(output) < 210:
                self.__lines += 2
            elif len(output) < 280:
                self.__lines += 3
            elif len(output) < 350:
                self.__lines += 4
            elif len(output) < 420:
                self.__lines += 5
            elif len(output) < 490:
                self.__lines += 6
            elif len(output) < 560:
                self.__lines += 7
            elif len(output) < 630:
                self.__lines += 8
            elif len(output) < 700:
                self.__lines += 9
            elif len(output) < 770:
                self.__lines += 10
            elif len(output) < 840:
                self.__lines += 11
            elif len(output) < 910:
                self.__lines += 12
            elif len(output) < 980:
                self.__lines += 13
            else:
                pass
        except:
            # user doesn't have the item to acces the room
            #print("Error checking room/inventory")
            pass
        if self.__lines >= 22:
            store = currentOutput.split("\n")
            if len(userInput) < 70:
                del store[0:2]
            elif len(userInput) < 140:
                del store[0:3]
            elif len(userInput) < 210:
                del store[0:4]
            else:
                del store[0:5]
            currentOutput = ""
            for item in store:
                currentOutput = currentOutput + "\n" + item

            if len(output) < 70:
                pass
            elif len(output) < 140:
                del store[0]
            elif len(output) < 210:
                del store[0:2]
            elif len(output) < 280:
                del store[0:3]
            elif len(output) < 350:
                del store[0:4]
            elif len(output) < 420:
                del store[0:5]
            elif len(output) < 490:
                del store[0:6]
            elif len(output) < 560:
                del store[0:7]
            elif len(output) < 630:
                del store[0:8]
            elif len(output) < 700:
                del store[0:9]
            elif len(output) < 770:
                del store[0:10]
            elif len(output) < 840:
                del store[0:11]
            elif len(output) < 910:
                del store[0:12]
            elif len(output) < 980:
                del store[0:13]
            else:
                del store[0:14]
                
        if outputCut[1] == ' ':
            win = winningScreen.WinningScreen()
            self.master.destroy()
            win.mainloop()
        else:
            pass

        self.__outputStore = (currentOutput + "\n>>>" + str(userInput) + "\n" +
            output)
        self.__output.set(self.__outputStore.lstrip("\n"))
        self.__commandLine.delete(0, END)

    def __init__(self):

        #Initialization of the main base GUI
        mainUI = Tk() #Main GUI
        Frame.__init__(self) #GUI frame
        self.master.title("Chronophobia") #Title of GUI (Showed on window)
        self.master.geometry("620x385") #Dimensions of GUI window
        self.grid(padx = 0, pady = 0) #Defining how much room should be between
                                      #widgits

        #Variables to be used later
        self.__turnsLeft = 100
        self.__turns = StringVar()
        self.__turns.set(self.__turnsLeft) #Setting a StringVars for use in
        self.__output = StringVar()        #turn counter and output feed.
        self.__outputStore ="Chronophobia Ver 1.05, 12/12/2015" + \
                            "\n>>>Welcome to Chronophobia!" + \
                            "\nYou stand up from your place on the floor and "\
                            "take a moment to collect yourself. Your head "\
                            "throbs with an unknowing pain as you try to get "\
                            "a good look of your surroundings."
        self.__output.set(self.__outputStore)
        self.__lines = 0
        self.__currentRoom = "lobby"
        self.__inventory = list()
        self.__invent = StringVar()
        self.__invent.set(self.__inventory)


        #Creating the event feed frame to hold the output
        self.__outputFeedFrame = LabelFrame(mainUI, text = "Event Feed",
                                    height = "350", width = "500",
                                    fg = "black")
        self.__outputFeedFrame.grid_configure(column = 1, rowspan = 2)

        #Initializing the actual feed (not done yet)
        self.__outputFeed = Label(self.__outputFeedFrame, height = 22,
        width = 70, wraplength = 500, bg = "white", fg = "black", anchor = NW,
        justify = LEFT, textvariable = self.__output)
        self.__outputFeed.pack(side = LEFT)

        #Initializing the command entry line
        self.__commandLine = Entry(mainUI, width = "82") #Setting dimensions
        self.__commandLine.grid(column = 1, row = 3) #Setting location

        #initializing the turn counter frame
        self.__turnCounterFrame = LabelFrame(mainUI, text = "Turns remaining",
                                        height = "100", width = "100")
        self.__turnCounterFrame.grid(column = 2, row = 1)

        #Initializing the turn counter
        self.__turnCount = Label(self.__turnCounterFrame,
                                textvariable = self.__turns)
        self.__turnCount.pack() #This is to actually display the text

        #Initializing the inventory
        self.__inventoryFrame = LabelFrame(mainUI, text = "Inventory",
                                    height = "300", width = "100")
        self.__inventoryFrame.grid(column = 2, row = 2)

        self.__inventoryLabel = Label(self.__inventoryFrame, height = 15,
                    width = 15, textvariable = self.__invent, bg = "white",
                    anchor = N)
        self.__inventoryLabel.pack()
        #Adding submit button
        self.__submitButton = Button(mainUI, text = "Submit", width = 10,
            command = lambda: self.commandSubmit(0))
            #"Command" is to attach function to button.

        #Binding 'enter' to commandSubmit function
        self.__submitButton.grid(row = 3, column = 2)
        mainUI.bind(sequence = '<Return>', func = self.commandSubmit)
