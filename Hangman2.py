# import random
# import turtle

# class Hangman:

#     fin = open("wordlist.txt","r")
#     words = [i.strip() for i in fin.readlines()]

#     def __init__(self):
        
#         self.numPlayers = int(input("Enter the number of players (1/2): \n"))

#         if (self.numPlayers==1):
#             self.oneP()
#         elif (self.numPlayers==2):
#             self.twoP()
#         else:
#             print("Please enter a valid number.\n")

#     def oneP(self):
#         print("You will now play against the computer.")
#         self.customWords = []
#         yn = input("Would you like to make your own custom words? (y/n)\n").strip().lower()
#         if (yn=="y"):
#             self.cWord=random.choice(self.words) #WIP
#         else:
#             self.cWord = random.choice(self.words)
#         print(self.cWord)

#     def twoP(self):
#         print("twoP")


# while (True): 
#     game = Hangman()
#     yn = input("Do you want to play again? (y/n)\n").strip().lower()
#     if not yn=="y":
#         break

# # draw_hangman feature
# # one player_game
# # two play_game

from tkinter import *
from PIL import ImageTk, Image
import time

class Graphics(Canvas):

    pics = {
        '1':'backgrounds/step1.png',
        '2':'backgrounds/step2.png',
        '3':'backgrounds/step3.png',
        '4':'backgrounds/step4.png',
        '5':'backgrounds/step5.png',
        '6':'backgrounds/step6.png',
        '7':'backgrounds/step7.png'
    }

    def __init__(self, master):

        self.width=500
        self.height=550

        Canvas.__init__(self, master, bg='saddle brown', width=self.width, height=self.height, highlightthickness=0)

        self.step = '1'
        self.createImage(self.step)
        self.limit='7'

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
        if self.step==self.limit:
            return
        self.step = str(int(self.step)+1)
        self.delete(self.pic)
        self.createImage(self.step)
        self.after(500, self.nextStep)

class Hangman(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()

        self.graphics = Graphics(self)
        self.graphics.grid(row=0,column=0)

        self.after(500, self.graphics.nextStep)

        



def play_hangman():
    root = Tk()
    root.title='Hangman'
    game = Hangman(root)
    root.mainloop()

play_hangman()