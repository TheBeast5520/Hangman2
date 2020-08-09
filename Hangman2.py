from tkinter import *
from PIL import ImageTk, Image
import time

pause=100

class Graphics(Canvas):

    pics = {
        '1':'backgrounds/step1.png',
        '2':'backgrounds/step2.png',
        '3':'backgrounds/step3.png',
        '4':'backgrounds/step4.png',
        '5':'backgrounds/step5.png',
        '6':'backgrounds/step6.png',
        '7':'backgrounds/step7.png',
        '8':'backgrounds/step8.png',
        '9':'backgrounds/step9.png',
        '10':'backgrounds/step10.png',
        '11':'backgrounds/step11.png',
        '12':'backgrounds/step12.png'
    }

    def __init__(self, master):

        self.width=500
        self.height=550

        Canvas.__init__(self, master, bg='saddle brown', width=self.width, height=self.height, highlightthickness=0)

        self.step = '1'
        self.createImage(self.step)

    def createImage(self,picName,size=()):
        if size==():
            size=(self.width,self.height)
        filename = self.pics[picName]
        self.im = Image.open(filename)
        self.resizePic(size)
        self.img=ImageTk.PhotoImage(self.im)
        self.pic = self.create_image(self.width/2,self.height/2,anchor=CENTER,\
                                     image=self.img)

    def resizePic(self,size):
        self.im = self.im.resize(size,Image.ANTIALIAS)

    def nextStep(self):
        if self.step=='6':
            self.after(pause, self.master.welcome)
            return
        self.step = str(int(self.step)+1)
        self.delete(self.pic)
        self.createImage(self.step)
        self.after(pause, self.nextStep)

class TEXT(Canvas):

    def __init__(self, master, width, height, text, anchor=CENTER,font=("eraser", 24), bg='black'):

        Canvas.__init__(self, master, bg=bg,width=width,height=height,highlightthickness=5)
        self.text = self.create_text(width/2,height/2,anchor = anchor, text=text, fill='white', font = font,justify=CENTER)


class BUTTON(Canvas):

    def __init__(self, master, width, height, text, command, anchor=CENTER, font=("eraser", 40), bg='black', relief=RAISED, key=""):

        Canvas.__init__(self, master, bg=bg,width=width, height=height, highlightthickness=5, relief=relief)
        self.text = self.create_text(width/2,height/2,anchor = anchor, text=text, fill='white', font = font,justify=CENTER)
        self.bind("<Button-1>", command)
        if (key != ""):
            self.bind(key, command)

class Hangman(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()

        self.graphics = Graphics(self)
        self.graphics.grid(row=0,column=0,rowspan=10)

        self.after(pause, self.graphics.nextStep)

        
    def welcome(self):
        self.welc = TEXT(self, 400, 550, text="Welcome\nto\nHANGMAN!",font=("eraser", 40))
        self.welc.grid(row=0,column=1,rowspan=10)
        self.after(pause, self.rWgO)

    def rWgO(self):
        self.welc.grid_remove()
        self.welc.grid_remove()
        self.onePlayer = BUTTON(self, width=400, height=550/2, text="ONE-PLAYER", command=self.one_player, relief=GROOVE)
        self.onePlayer.grid(row=0,column=1,rowspan=5)
        self.twoPlayer = BUTTON(self, width=400, height=550/2, text="TWO-PLAYER", command=self.two_player, relief=GROOVE)
        self.twoPlayer.grid(row=5,column=1,rowspan=5)

    def one_player(self, misc=""):
        # self.onePlayer.grid_remove()
        # self.twoPlayer.grid_remove()
        print("one_player")


    def two_player(self, misc=""):
        print("two_player")
        self.name1 = INPUT()


def play_hangman():
    root = Tk()
    root.title='Hangman'
    game = Hangman(root)
    root.mainloop()

play_hangman()