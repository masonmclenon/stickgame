'''
Name: Mason McLenon
Section: D
Project: HW 4, Pictsie Sticks Game
Description: A game where two players take up to 3 sticks from 20 starting sticks
that ends when a player loses by taking the last stick. Every round has a 30% chance 
of regenerating 1 to 4 sticks to the total sticks in play.
'''
import random

#function which displays the board with the input being the amount of sticks in play
def display_board(sticks):
    count = 1
    print("")
    #Creates the lines to form sticks
    while count < 6:
        for i in range(1,sticks+1):
            print(" {:>2} ".format("|"),end="")
        print("")
        count += 1
    #Creates the numbers under the sticks indicating their respective number
    for i in range(1,sticks+1):
        print(" {:>2} ".format(i),end="")
    print("\n")

#function which indicates the players turn, and allows them to take up to 3 sticks and returns this number
def take_sticks(player,sticks):
    loop = True
    print("Player {}'s turn".format(player))
    #Continually runs until correct input is entered by the player
    while loop == True:
        sticks_chosen = int(input("Enter total sticks you'll remove (up to 3).\n"))
        if sticks_chosen >= 1 and sticks_chosen <= 3 and sticks_chosen <= sticks:
            loop = False
            return sticks_chosen
        #Indicates the user cannot take more sticks than there are in play
        elif sticks_chosen > sticks:
            print("There's not that many sticks left!")
        else:
            print("Invalid input. Enter 1, 2 or 3.")

#function which determines if any extra sticks are added to the sticks in play
def not_quite_right(sticks):
    chance = random.randint(1,10)
    sticks_returned = 0
    #30% chance that this code will run, generating a number between 1 and 4 and adding it to the total sticks in play
    if chance > 7:
        sticks_returned = random.randint(1,4)
        sticks += sticks_returned
        #Ensures the maximum amount of sticks added does not bring the total sticks in play above 20
        while sticks > 20:
            sticks -= 1
            sticks_returned -= 1
        return sticks_returned
    else:
        return sticks_returned

#function which displays which player took how many sticks and if the pictsie magic added any back including the amount, along with the total remaining sticks in play
def display_summary(player_turn, sticks_taken, sticks_added, sticks):
    print("Player {0}'s took {1} stick, pictsie magic added {2} sticks back, leaving {3} sticks".format(player_turn, sticks_taken, sticks_added, sticks))

def main():
    #player_turn's value will change depending upon if it is player 1 or player 2's turn.
    player_turn = 1
    #sticks holds the value of the total sticks still in play
    sticks = 20
    #sticks_taken will hold the return value of the take_sticks function
    sticks_taken = 0
    #sticks_added will hold the return value of the not_quite_right function
    sticks_added = 0

    #Loop which creates the turns for the players and then ends the game when sticks run out
    while player_turn != 0:
        #A turn for player 1
        while player_turn == 1:
            if sticks > 0:
                display_board(sticks)
                sticks_taken = take_sticks(player_turn,sticks)
                #subtracts the amount of sticks taken from the amount of sticks in play
                sticks -= sticks_taken
                sticks_added = not_quite_right(sticks)
                #adds the amount of sticks returned from the not_quite_right function to the amount of sticks in play
                sticks += sticks_added
                display_summary(player_turn, sticks_taken, sticks_added, sticks)
                #changes the turn to player 2
                player_turn = 2
            else:
                print("Player 1 won the game since player 2 took the last stick!")
                #ends the game
                player_turn = 0
        #A turn for player 2
        while player_turn == 2:
            if sticks > 0:
                display_board(sticks)
                sticks_taken = take_sticks(player_turn,sticks)
                sticks -= sticks_taken
                sticks_added = not_quite_right(sticks)
                sticks += sticks_added
                display_summary(player_turn, sticks_taken, sticks_added, sticks)
                #changes the turn to player 1
                player_turn = 1
            else:
                print("Player 2 won the game since player 1 took the last stick!")
                #ends the game
                player_turn = 0

main()
