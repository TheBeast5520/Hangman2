
class Hangman:

    def __init__(self):
        
        self.numPlayers = int(input("Enter the number of players (1/2): \n"))

        if (self.numPlayers==1):
            self.oneP()
        elif (self.numPlayers==2):
            self.twoP()
        else:
            print("Please enter a valid number.\n")

    def oneP(X):
        print("oneP")

    def twoP(self):
        print("twoP")


while (True): 
    yn = input("Do you want to play again?\n").strip().lower()
    if not yn=="yes":
        break
    game = Hangman()

# draw_hangman feature
# one player_game
# two play_game
