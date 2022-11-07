# algorithim 
# user inputs a word or sentace
# the input is then converted into a list
# the list is iterated through, finding the current letter in a lookup dict
# the letter that returns from this is added to a string
# the string is returned
# and printed

import time
import os

#the function!!!!!!!!!!
def toNatoPhonetic(text=None):
    if text==None: return False

    lookup_table = {
        'a':'Alfa',
        'b':'Bravo',
        'c':'Charlie',
        'd':'Delta',
        'e':'Echo',
        'f':'Foxtrot',
        'g':'Golf',
        'h':'Hotel',
        'i':'India',
        'j':'Juliett',
        'k':'Kilo',
        'l':'Lima',
        'm':'Mike',
        'n':'November',
        'o':'Oscar',
        'p':'Papa',
        'q':'Quebec',
        'r':'Romeo',
        's':'Sierra',
        't':'Tango',
        'u':'Uniform',
        'v':'Victor',
        'w':'Whiskey',
        'x':'X-ray',
        'y':'Yankee',
        'z':'Zulu',
        '1':'One',
        '2':'Two',
        '3':'Three',
        '4':'Four',
        '5':'Five',
        '6':'Six',
        '7':'Seven',
        '8':'Eight',
        '9':'Nine',
        '0':'Zero',
    }

    #convert the text to lower and initialize the return varible
    lower_text = text.lower()
    natoWord = ''

    #iterate though the text
    for i in lower_text:
        try:
            #search the lookiup table for the current charicter
            phoneme = lookup_table[i]

            #add it to the list
            natoWord += phoneme.capitalize() + ' '
        
        except KeyError:
            #incase the current charicter is not in the lookup table
            #also kinda just stops errors from happening :)
            pass

    
    return natoWord

def toMorse(text=None):
    #this function is literally the same thing as to the fucntion above, diffrent table and return value formating
    if text==None: return False

    lookup_table = {
        'a':'.-',
        'b':'-...',
        'c':'-.-.',
        'd':'-..',
        'e':'.',
        'f':'..-.',
        'g':'--.',
        'h':'....',
        'i':'..',
        'j':'.---',
        'k':'-.-',
        'l':'.-..',
        'm':'--',
        'n':'-.',
        'o':'---',
        'p':'.--.',
        'q':'--.-',
        'r':'.-.',
        's':'...',
        't':'-',
        'u':'..-',
        'v':'...-',
        'w':'.--',
        'x':'-..-',
        'y':'-.--',
        'z':'--..',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----',
    }

    lower_text = text.lower()
    word = ''

    for i in lower_text:
        
        try:
            char = lookup_table[i]
            word += char
        except KeyError:
            pass
    
    return word

#main function
def main():

    #welcome text and command list + syntax
    print('welcome to govement subsidezed text conversion software.')
    print('please input what you will like to convert to:')
    print("""
        SYNTAX:     :n sample text
    
        :n          <= string to nato phonetic
        :mc         <= string to morse code
    
        :tbl        <= nato conversion table
        :mctbl      <= morse code converson table
        :q          <= to quit
        :cls        <= clears the screen
    """)

    while True:
        user_action = input('')

        #check if the command is in the input, reqireed due to the :n && :mc commands having more then just the command name
        #yes they are written in a vim instpired style, fight me

        if ":n" in user_action:
            text = user_action.removeprefix(':n ')
            translated = toNatoPhonetic(text)
            print(translated)
        elif ':tbl' in user_action:
            lookup_table = {
                'a':'Alfa',
                'b':'Bravo',
                'c':'Charlie',
                'd':'Delta',
                'e':'Echo',
                'f':'Foxtrot',
                'g':'Golf',
                'h':'Hotel',
                'i':'India',
                'j':'Juliett',
                'k':'Kilo',
                'l':'Lima',
                'm':'Mike',
                'n':'November',
                'o':'Oscar',
                'p':'Papa',
                'q':'Quebec',
                'r':'Romeo',
                's':'Sierra',
                't':'Tango',
                'u':'Uniform',
                'v':'Victor',
                'w':'Whiskey',
                'x':'X-ray',
                'y':'Yankee',
                'z':'Zulu',
                '1':'One',
                '2':'Two',
                '3':'Three',
                '4':'Four',
                '5':'Five',
                '6':'Six',
                '7':'Seven',
                '8':'Eight',
                '9':'Nine',
                '0':'Zero',
            }

            for i in lookup_table:
                print(f'{i}: {lookup_table[i]}') 
        elif ':mctbl' in user_action:
            lookup_table = {
                'a':'.-',
                'b':'-...',
                'c':'-.-.',
                'd':'-..',
                'e':'.',
                'f':'..-.',
                'g':'--.',
                'h':'....',
                'i':'..',
                'j':'.---',
                'k':'-.-',
                'l':'.-..',
                'm':'--',
                'n':'-.',
                'o':'---',
                'p':'.--.',
                'q':'--.-',
                'r':'.-.',
                's':'...',
                't':'-',
                'u':'..-',
                'v':'...-',
                'w':'.--',
                'x':'-..-',
                'y':'-.--',
                'z':'--..',
                '1':'.----',
                '2':'..---',
                '3':'...--',
                '4':'....-',
                '5':'.....',
                '6':'-....',
                '7':'--...',
                '8':'---..',
                '9':'----.',
                '0':'-----',
            }

            for i in lookup_table: print(f'{i}: {lookup_table[i]}')
        elif ':mc' in user_action:
            text = user_action.removeprefix(':mc ')
            translated = toMorse(text)
            print(translated)
        elif user_action == ':q':
            print('closing...')
            exit()
        elif user_action == ':cls':
            print('clearing screen...')
            time.sleep(0.25)
            os.system('cls')
        else: print('command not recognized!')


if __name__ == "__main__":
    main()
