# CHALLENGE 3: Dice Game
# Create a DICE GAME FUNCTION:
# Output has 3 columns in a table: “You, Me, and Winner”
# Use random numbers (range 1,7) to generate dice roll for columns 1 and 2
# Decide winner for each role (or a tie) and output in the third column
# *You can run the game multiple times with a pre-set FOR loop, or you can use a WHILE loop to ask if user wants to play again.

import random

def roll():
    """this function returns 2 diffrent dice rolls"""
    return [random.randrange(1, 7), random.randrange(1, 7)]

def print_game_log(log=None, p1name=None):
    """this function prints out the gamelog as a 'spreadsheet' with custon formatting"""

    print()
    print(f'PLAYER 1 NAME: {p1name}')

    if log==None: return False

    print("GAME LOG:")
    print("PLAYER 1  |  PLAYER 2  |  WINNER")
    print("--------------------------------")

    for i in log:
        print(f'{i["p1"]}         |  {i["p2"]}         |  {i["win"]}')


def main():
    """this is the main function lol"""

    #devfine placeholder names for both players
    player1 = 'player ONE'
    player2 = 'player TWO'

    #iniialize the game log
    game_log = []

    #get the player one username
    username = input('please enter a username: ')
    player1 = username

    while True:

        #make the roll
        r1, r2 = roll()

        #figure out who won
        if r1 > r2:
            winnner = player1
        elif r2 > r1:
            winnner = player2 
        else:
            winnner = 'TIE'
        
        #add it to game log
        game_log.append({"p1":r1, "p2":r2, "win":winnner})

        #print out the results
        print(f'you rolled a: {r1}',  f'opponent rolled a: {r2}', f'the winner is: {winnner}')
        print()

        #ask the user if they want to play again
        user = input('do you want to play again? (y/n) ')
        if user == 'n':

            #if not, print out the game log
            print_game_log(game_log, username)
            break


if __name__ == "__main__":
    main()