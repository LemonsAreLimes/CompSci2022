# game loop
    # intializations: 
        # wrong letters
        # completed letters in word
        # word
    
    # loop
        # check if the user has won or lost
        # if won: print win screen
        # if lose: print lose screen
        # else: 
            # get the user to input a charicter (loop + try/except because user might not input right one + if already used)
            # check if its in the word
                # true: edit the completed letters
                # false: chances++ && wrong letters.append

from os import system as sys
from os import name as osName
from random import randint

def initalize():
    
    word_list = [
        'this',
        'is ',
        'so ',
        'great ',
        'typing',
        'out ',
        'a ',
        'bunch',
        'of',
        'words',
        'no',
        'im ',
        'not ',
        'going ',
        'to ',
        'do',
        'add',
        'another',
        'thing ',
        'onto',
        'words',
        'because',
        'lazyness',
    ]

    return word_list[randint(0, len(word_list))]


def convertLettersToWord(letter_list, word):

    # get the used positions
    used_positions = []

    # iterate though all the letters in the list
    for char in range(len(letter_list)):
        
        # iterate though the word
        for pos in range(len(word)):

            # check if the charicter is the selected one? 
            if word[pos] == letter_list[char]:
                used_positions.append(pos)

    # actually edit the word
    new_word = ''
    for i in range(len(word)):
        if i not in used_positions:
            new_word += '_'
        else:
            new_word += word[i]

    return new_word



def game(word=None):
    if word==None: print('something went wrong!'); return
    wrong_awesers = []
    correct_awensers = []
    converted_correct = ''
    chances = 0

    # print out the welcome message
    print('welcome to hangman prototype, from EG games.')
    print('to save this man you must geuss the correct word!')

    # main game loop
    while True:

        #determine what to print
        if converted_correct != '':
            print()
            print(converted_correct)

        if chances != 0:
            print(f' these are wrong: {wrong_awesers}, you have: {10 - chances} chances left!' )
            print()

        # check if the user has won or lost
        if chances >= 10:                 
            print('you have run out of chances!')
            exit()
        
        elif converted_correct == word:                     
            print('you have won!')
            exit()

        # if not, enter the input loop
        else:                  
            while True:
                    
                    print()
                    letter = input('choose a letter: ')

                    # check if the input is a letter
                    if letter.lower() not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                        print('the charicter is not a letter, please try again!')

                    # check if the input has already been used => do not deduct points
                    elif letter in wrong_awesers or letter in correct_awensers:
                        print('you have already used this charicter')
    
                    # check if the letter is in the word
                    elif letter in word: 
                        correct_awensers.append(letter)
                        converted_correct = convertLettersToWord(correct_awensers, word)        #convert the list to a string, set it as the new
                        print(f'"{letter}" is in the word!')
                        print(converted_correct)
                        sys('cls' if osName =='nt' else 'clear')
                        break

                    else:
                        wrong_awesers.append(letter)
                        chances += 1
                        print('that is not correct!')
                        print(f'you have {10 - chances} left') 
                        sys('cls' if osName =='nt' else 'clear')
                        break



if __name__ == '__main__':

    selected_word = initalize()
    game(selected_word)