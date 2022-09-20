import random


#function Calculates total cost with GST
def calc_total(inital_cost=None, discount=None):                                
    
    #check if all perameters are set
    if inital_cost == None or discount == None: return False

    # Return actual amount customer pays (add GST then subtract discount)
    return round(inital_cost * 1.05 - inital_cost * discount, 2)         


#get the input cost
item_1 = float(input('please enter in the ammount of first purchase: '))
item_2 = float(input('please enter in the ammount of seccond purchase: '))
item_3 = float(input('please enter in the ammount of third purchase: '))
item_total = item_1 + item_2 + item_3

print()
print(f"the total comes out to around ${ round(item_total, 2) }")

#generate a random discount
rand_discount = random.randrange(10, 40, 5) / 100
print(f'with the week-long random discount event, you get a discount of: { rand_discount * 100 }%')
print(f'after gst the discount comes out to: { round((rand_discount - 0.05) * 100, 2)}%')
print()

#call the calc_total function, set its return as discount_tax_total
discount_tax_total = calc_total(inital_cost=item_total, discount=rand_discount) 

#print out succsess message
print(f'your final purcase price with a discount of { rand_discount * 100 }% comes out to: ${ discount_tax_total }')
print()