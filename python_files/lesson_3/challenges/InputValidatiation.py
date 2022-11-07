# CHALLENGE 2: Function for Validating Input (Yes or No)
# You want the user to enter Y or N (upper or lower) for a Yes/ No question
# While loop will keep asking until it receives a valid answer (Hint: use boolean True/ False to control the WHILE loop)
# Program will use .upper() conversion
# Copy and Past your Source Code on the Lesson 3 Challenges Google Doc
# Copy and Paste your terminal window output

import random
import colorama

def main():

    while True:

        print() 
        user = input('do you want to delete system32? (y/n)')

        if user.upper() == 'Y':
            print('deleting system 32! please do not turn off your computer')

            abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0",]
            while True:

                new = f'{colorama.Fore.RED}'
                for i in range(200):
                    char = abc[random.randrange(0, len(abc))]
                    new += char

                print(new)

        else:
            print('thats not the correct awenser!')



if __name__ == "__main__":
    main()