from tkinter import *

class WinningScreen(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.top = Tk()
        self.win = Label(self.top,
        text = "You unlock the three locks and the door slowly"\
               " opens.\nYou rush out and stop running by the "\
               "street.\nTurning back you see the mannequin "\
               "right next to you.\nIt begins to whisper...\n"\
               "J̕͝͠u̡͢͜ş̸t b̀e̷c̀a̶͢ù̢s͢ȩ̡̕ ͞ỳ̧o͝͠u'r͞è͞ ̢͠"\
               "͢b͡re͏̴a͜͏t̡h̨́i̸̕ǹ͟g̀,͠ d̨́ǫ́͠es͟͠n͢͝'̢͏t̷͟ ̡̕"\
               "͝m͜͟e͏a̡n̨͢ yo̷u͏'̷́͢re̡̨ ̡́aliv̡̕͝e͞͠͝.̷͟ ")
        self.gameQuit = Button(self.top, text = "OK",
                                command = self.top.destroy)
        self.win.pack()
        self.gameQuit.pack()
    
