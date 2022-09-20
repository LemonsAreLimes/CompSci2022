
            # Cashier System



from random import randrange
import time


# Function 1: User inputs name and cost of each item (Example: Cat Food $7.99)
def get_item():
    item_name = input('name of item: ')
    item_cost = input('cost of item: ')
    print()


    item_cost_parsed = float(item_cost)


    #add it to an object so it can be returned
    item_data = {
        "name":item_name,
        "cost":item_cost_parsed
    }

    return item_data

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
            item = get_item()           
            
            #check if the func acctually returned an object
            if item != False:
                counter += 1
                item_log.append(item)

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


    for item in items_bought:

        #format the name
        formatted_name = item['name']
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
    print()
    print(f'however, we are offering a discount of {rand_discount * 100}%')
    print()

    # Apply a random Discount (10, 20, 30 %)
    print(f'your total comes out to: {round(total_cost * rand_discount, 2)}')

# Function 2: Advertising Graphic included at the end with store logo design and on screen message (turtle graphics!)
def play_logo_animation():
    for i in range(1000):
        time.sleep(0.01)

        print(i, end='\r')  #\r is a return charicter (lets you print over currently printed stuff )


#the main function
def main():

    # Welcome message
    print('''
    
        welcome message
            -lorem ipsum
    
    ''')

    #this loop is basically for if the user inputs in an invalid ammount
    while True:     

        item_ammount = input('enter in the ammount of items you will be buying: ')

        try:
            # User inputs how many items they will be purchasing
            item_ammount = float(item_ammount)
    
            #call a function that askes the user for each item ammount and its name
            recipt_data = item_collector(item_ammount=item_ammount)
            if recipt_data == False: print('MALFUNCTION 54')

            #print out the recipt
            print_recipt(items_bought=recipt_data)
            break

        except:
            print('invalid input type!')

    #play the logo animation
    play_logo_animation() 


if __name__ == "__main__":
    main()