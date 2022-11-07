# print out welcome message + todays special
# print out the standard pizzas (cheese, peperoni, hawaiian.. etc)
# get the input
# get the size of the pizza
# chose / edit the toppings (add/remove) => on each change reprint
# when done all of this
# get the deli addy
# get the time and estimate deli time +- 10 min of 30
# print out the recept

from random import *
import time

def selectStandard():
    specials = [
        ['chefs Disaster', ['spagetti', 'spagetti sauce']],
        ['hawiian', ['pineapple']],
        ['burger pizza', ['burger']],
        ['nothing', ['no cheese', 'no toppings', 'no sauce', 'bread']],
    ]
    today_special = specials[randint(0, len(specials)-1)]

    # print welcome message and today's special
    print('welcome to pizza, where we serve pizza and pizza')
    print(f'todays special is: {today_special[0]}')
    print()
    use_special = input('would you like to try todays special? (y/n) ')
    
    # if is special return it
    if use_special == 'y': 
        return today_special

    # if not, print out standard pizzas
    standards = [
        ["peperoni",    ['peperoni']],        # name, toppings
        ["meat lovers", ['peperoni','salami']],
        ["hawaiaan",    ['spam','pineapple']],
        ["vegan",       ['spincach',]]
    ]

    print()
    print('would you like to try any of these?')
    print()
    print('0: none')

    # print out the pizzas
    for i in range(len(standards)):
        print(f'{i + 1}: {standards[i][0]}')
    
    print()
    
    # get the user input for the pizza
    while True:
        select = input('select witch pizza you would like: ')
        if select == '0': return False
        elif select.isnumeric() and int(select) > len(standards): print('list index out of range!'); continue
        elif select.isnumeric(): return standards[int(select)-1]
        else: continue

def getSize():

    # print out the sizes
    print('what size would you like?')
    print("0: small    10'")
    print("1: medium   12'")
    print("2: large    15'")

    sizes = [
        ['small', 15],
        ['medium', 20],
        ['large', 30],
    ]

    # get the input
    while True:
        size_cmd = input('size: ')
        
        if size_cmd.isnumeric():
            if int(size_cmd) > len(sizes) or int(size_cmd) < 0: print('thats not on the list!')
            else:                                               return sizes[int(size_cmd)]

        else: continue

def getTopping(pizza):
    
    # ask the user if they want toppings
    print()
    if input('would you like to add more toppings? (y/n) ') == 'n': return pizza

    # enter the edit loop
    avalable_toppings = [
        'peperoni',
        'salami',
        'brocoli',
        'pizza',
        'pineapple',
        'spam',
        'mustard',
        'extra cheese',
        'air',
    ]
    selected_toppings = pizza[1]

    while True:
        print(f'current toppings: {selected_toppings}')
        print()
        print('avalable toppings')

        print('0: save && exit')
        for i in range(len(avalable_toppings)):
            print(f'{i+1}: {avalable_toppings[i]}')

        # get the user input
        command = input('add or remove: ')

        # make sure the command is a number and in rang
        if command == '0': return selected_toppings
        elif command.isnumeric() == False: print('please enter an index!'); continue
        elif int(command)-1 > len(avalable_toppings): print('list index out of range!'); continue

        # check if the topping is in the selected, remove.... this is a little bit buggy but still *technically* works
        elif avalable_toppings[int(command)-1] in selected_toppings:

            # find the topping in selected
            for i in range(len(selected_toppings)-1):
                if avalable_toppings[int(command)-1] == selected_toppings[i]:
                    selected_toppings.pop(i)
                    
        # if the selected topping is not in the list, add to it
        elif avalable_toppings[int(command)-1] not in selected_toppings:
            selected_toppings.append(avalable_toppings[int(command)-1])

        else: print('command not recognized!'); continue

def calcPrice(toppings, size):

    # price of toppings + size price
    topping_price = len(toppings) * 2
    size_price = size[1]

    return topping_price + size_price

def printRecept(pizza, size, toppings):
    
    print()
    print('_______RECEPT_______')
    print(f'a standard: {pizza[0]}')
    print(f'with a size of: {size[0]}')
    print(f'toppings: ')
    
    for i in toppings[1]:
        print('   ' + i)

    print('_______RECEPT_______')
    print(f'total: ${calcPrice(toppings, size)}.99')
    print()

    print('please enter in your address')
    addy = input()

    unix_time = int(time.time()) + 1800
    messy_time = time.localtime(unix_time)

    print(f'okay great! you pizza will be delivered at: {messy_time.tm_hour}:{messy_time.tm_min}')


def main():

    pizza = selectStandard()
    size = getSize()
    toppings = getTopping(pizza)
    printRecept(pizza, size, toppings)


if __name__ == "__main__":
    main()