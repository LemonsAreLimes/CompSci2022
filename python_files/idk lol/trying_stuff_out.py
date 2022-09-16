
#the function => basically ammount - (deduct_1 + deduct_2)
def how_much_money_do_i_got(ammount=None, deduct_1=None, deduct_2=None):
    
    #check that all perameters are satisfied and not empty (prevents invalid positional argument errors) in cli apps or something
    if ammount != None and deduct_1 != None and deduct_2 !=None:
        
        #check if the user inputted the numbers in correctly
        try:
            float(ammount)
            float(deduct_1)
            float(deduct_2)
        except ValueError:
            print('inalid values inputted, pls use NUMBERS')
            return False

        #do the calculation and tell me what it is
        cash_left = float(ammount) - float(deduct_1) - float(deduct_2)
        return cash_left


#get the requred values    
money =     input('input the deposit ammount:')
rent =      input('input the monthly rent: ')
groceries = input('input the groceries ammount: ')

#throw them into the function
cash_left = how_much_money_do_i_got(money, rent, groceries)

#make sure its dosent return the fail value
if cash_left != False:

    #update money
    money = cash_left
    print(money)
