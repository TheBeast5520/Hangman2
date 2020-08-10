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

    def __init__(self, master, width, height, text, anchor=CENTER,font=("Autography", 24), bg='black'):

        Canvas.__init__(self, master, bg=bg,width=width,height=height,highlightthickness=5)
        self.text = self.create_text(width/2,height/2,anchor = anchor, text=text, fill='white', font = font,justify=CENTER)


class BUTTON(Canvas):

    def __init__(self, master, width, height, text, command, anchor=CENTER, font=("Autography", 40), bg='black', relief=RAISED, key=""):

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

        self.background = TEXT(self, 400, 550, text="")
        self.background.grid(row=0,column=1,rowspan=10)

        self.after(pause, self.graphics.nextStep)

        
    def welcome(self):
        self.welc = TEXT(self, 400, 550, text="Welcome\nto\nHANGMAN!",font=("Autography", 40))
        self.welc.grid(row=0,column=1,rowspan=10)
        self.after(pause, self.rWgO)

    def rWgO(self):
        self.welc.grid_remove()
        self.welc.grid_remove()
        self.onePlayer = BUTTON(self, width=400, height=550/2, text="ONE-PLAYER", command=self.one_player, relief=GROOVE)
        self.onePlayer.grid(row=0,column=1,rowspan=5)
        self.twoPlayer = BUTTON(self, width=400, height=550/2, text="TWO-PLAYER", command=self.two_player1, relief=GROOVE)
        self.twoPlayer.grid(row=5,column=1,rowspan=5)

    def one_player(self, misc=""):
        # self.onePlayer.grid_remove()
        # self.twoPlayer.grid_remove()
        print("one_player")


    def two_player1(self, misc=""):
        self.onePlayer.grid_remove()
        self.twoPlayer.grid_remove()
        self.name1 = Entry(self, bg='black', font = ("Autography",30), justify=CENTER, fg='white')
        self.name1.insert(0,"""ENTER NAME-1 HERE""")
        self.name1.bind("<FocusIn>", self.delName1)
        self.name1.place(width=400, height=550/2, x=500+5, y=5, anchor=NW)
        self.name2 = Entry(self, bg='black', font = ("Autography",30), justify=CENTER, fg='white')
        self.name2.insert(0,"ENTER NAME-2 HERE")
        self.name2.bind("<FocusIn>", self.delName2)
        self.name2.place(width=400, height=550/2, x=500+5, y=5+550, anchor=SW)
        self.dButton = Button(self, bg='black', fg='white', font = ("Autography", 20), justify=CENTER, command=self.two_player2, text='continue')
        self.dButton.grid(row=10, column=1)
    
    def delName1(self, misc=""):
        self.name1.delete(0, END)
        self.name1.unbind("<FocusIn>")

    def delName2(self, misc=""):
        self.name2.delete(0, END)
        self.name2.unbind("<FocusIn>")

    def two_player2(self, misc=""):
        self.names=[self.name1.get(), self.name2.get()]
        self.name1.destroy()
        self.name2.destroy()
        self.dButton.grid_remove()

        # while True:



def play_hangman():
    root = Tk()
    root.title='Hangman'
    game = Hangman(root)
    root.mainloop()

play_hangman()