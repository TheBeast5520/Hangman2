import random
import turtle

class Hangman:

    fin = open("wordlist.txt","r")
    words = [i.strip() for i in fin.readlines()]

    def __init__(self):
        
        self.numPlayers = int(input("Enter the number of players (1/2): \n"))

        if (self.numPlayers==1):
            self.oneP()
        elif (self.numPlayers==2):
            self.twoP()
        else:
            print("Please enter a valid number.\n")

    def oneP(self):
        print("You will now play against the computer.")
        self.customWords = []
        yn = input("Would you like to make your own custom words? (y/n)\n").strip().lower()
        if (yn=="y"):
            self.cWord=random.choice(self.words) #WIP
        else:
            self.cWord = random.choice(self.words)
        print(self.cWord)

    def twoP(self):
        print("twoP")


while (True): 
    game = Hangman()
    yn = input("Do you want to play again? (y/n)\n").strip().lower()
    if not yn=="y":
        break

# draw_hangman feature
# one player_game
# two play_game
