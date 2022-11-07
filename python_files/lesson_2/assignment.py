from ctypes import wintypes
from random import randrange
import time
import turtle

# Function 1: User inputs name and cost of each item (Example: Cat Food $7.99)
def get_item(number=None):

    #get the anglicized version of the number
    if number == None:
        print('NUMBER NOT PROVIDED IN GET_ITEM!!!')

    nums = {1:'first',
            2:'seccond',
            3:'third',
            4:'fourth',
            5:'fith',
            6:'sixth',
            7:'seventh',
            8:'eighth',
            9:'ninth',
            10:'tenth',
            11:'eleventh',
            12:'twelvefth',
            13:'thirteenth',
            14:'fourteenth',
            15:'fifteenth',
            16:'sixteenth',
            17:'seventeenth',
            18:'eighteenth',
            19:'nineteenth',
            20:'twentyith'
        }
    num_to_use = nums[number+1]

    item_name = input(f'name of the {num_to_use} item: ')
    item_cost = input(f'cost of the {num_to_use} item: ')
    print()

    try:
        item_cost_parsed = float(item_cost)
        
        #add it to an object so it can be returned
        item_data = {
            "name":item_name,
            "cost":item_cost_parsed
        }

        return item_data
    
    except:
        return False

#asks the user for the item name and its price
def item_collector(item_ammount=None):
    if item_ammount == None: return False

    item_log = []
    counter = 0
    
    #collector for items
    while True:
        #this is requred as if someone inputs a wrong thing into the function the loop will keep flowing reguadless 
        if counter >= item_ammount:
            break
        
        else:
            # Program runs Function 1 the exact number of times for how many items purchased
            item = get_item(counter)           
            
            #check if the func acctually returned an object
            if item != False:
                counter += 1
                item_log.append(item)
            else:
                print('please try that again!')

    return item_log

#calculates the total clost with gst 
def get_total_cost(item_log=None, gst=1.05):
    if item_log == None: return False

    #accumelate the total cost
    total_cost = 0
    for item in item_log:
        total_cost += item['cost']

    #calculate the gst
    return total_cost * gst

# Item names and costs are printed out in an attractive statement at the end (This should look like a line by line receipt)
def print_recipt(items_bought=None):
    if items_bought == None: return False

    #calculate the longest name for formatting
    longest_name_len = 0

    for item in items_bought:
        if len(item['name']) > longest_name_len:
            longest_name_len = len(item['name'])

    print('----------------------RECIPT----------------------')

    #format the name
    for item in items_bought:    
        formatted_name = item['name'] + ' '
        for i in range(longest_name_len - len(item['name']) + 3):
            formatted_name += '-'

        #print out the name and cost
        cost = item['cost']
        print(f'item: {formatted_name} {cost}$')

    # Total, plus GST is calculated (accumulator pattern) and printed at the end of “receipt”
    total_cost = get_total_cost(item_log=items_bought)
    print()
    print(f'total after gst: {round(total_cost, 2)}')    

    #generate random discount
    rand_discount = randrange(10, 40, 5) / 100
    print(f'however, we are offering a discount of {rand_discount * 100}%')
    print()

    # Apply a random Discount (10, 20, 30 %)
    print(f'your total comes out to: {round(total_cost - (total_cost * rand_discount), 2)}')
    print('----------------------RECIPT----------------------')

# Function 2: Advertising Graphic included at the end with store logo design and on screen message (turtle graphics!)
def play_logo_animation():

    #initialization
    t = turtle.Turtle()
    window = turtle.Screen()
    t.pensize(10)
    t.shapesize(0.1)

    #made the commands into a list because its collapseable and takes up less space
    shape = [
        ['lt', 90],
        ['fd', 100],
        ['rt', 90],
        ['fd', 50],
        ['rt', 90],
        ['fd', 50],
        ['rt', 90],
        ['fd', 25],
        ['lt', 135],
        ['fd', 70],
        ['lt', 45],
        ['fd', 40],
        ['lt', 135],
        ['fd', 70],
        ['rt', 135],
        ['fd', 40],
        ['rt', 45],
        ['fd', 70],
        ['lt', 45],
        ['fd', 40],
        ['lt', 135],
        ['fd', 70],
        ['rt', 135],
        ['fd', 40],
        ['rt', 45],
        ['fd', 70],
    ]

    #parsing / drawing
    for i in shape:
        if i[0] == 'lt':
            t.lt(i[1])

        if i[0] == 'rt':
            t.rt(i[1])
        
        if i[0] == 'fd':
            t.fd(i[1])
    
    window.exitonclick()

#the main function
def main():

    # Welcome message
    print('                                                          :::   :::       :::     ::::::::: :::::::::::\n                                                        :+:+: :+:+:    :+: :+:   :+:    :+:    :+:\n      /____________________________________________   +:+ +:+:+ +:+  +:+   +:+  +:+    +:+    +:+\n     / :::::::::   ::::::::  :::    ::: ::::::::  /  +#+  +:+  +#+ +#++:++#++: +#++:++#:     +#+\n     :+:    :+: :+:    :+: :+:   :+: :+:    :+:  / +#+       +#+ +#+     +#+ +#+    +#+    +#+\n    +:+    +:+ +:+    +:+ +:+  +:+  +:+    +:+  / #+#       #+# #+#     #+# #+#    #+#    #+#\n   +#++:++#:  +#+    +:+ +#++:++   +#+    +:+  /###       ### ###     ### ###    ###    ### \n  +#+    +#+ +#+    +#+ +#+  +#+  +#+    +#+  /____________________________________________/\n #+#    #+# #+#    #+# #+#   #+# #+#    #+#  (baskilisk)                           -v4.19 /\n###    ###  ########  ###    ### ########')

    #this loop is basically used exclusivley if the user inputs a non-number in the item_ammount
    while True:     

        #inputs the ammount of items purchaced, in item_collector.
        item_ammount = input('input the ammount of items you will be purchasing: ')

        try:     
            #prevents user from inputing a non-number, hence try and catch block
            item_ammount = float(item_ammount)

            #make sure the item_ammount is not over 20. can change this later to like 1000 or something but for this its 20 
            if item_ammount >= 20:
                print('value cannot be above 20, our database is running on a 2014 android phone.')
                raise(ValueError)

            #call a function that askes the user for each item ammount and its name
            recipt_data = item_collector(item_ammount=item_ammount)
            if recipt_data == False: print('MALFUNCTION 54')

            #print out the recipt
            print_recipt(items_bought=recipt_data)
            break

        except:
            print('invalid input type!, remember it must be a number not a String')

    #play the logo animation
    play_logo_animation() 

#entry point
if __name__ == "__main__":
    main()