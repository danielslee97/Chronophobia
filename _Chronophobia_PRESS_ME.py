import TopMenu
import MainGui
def runGame():
    top = TopMenu.TopMenu()
    top.mainloop()
    if top.startGame == 1:
        mainGame = MainGui.MainGui()
        mainGame.mainloop()

def main():
    runGame()

main()
