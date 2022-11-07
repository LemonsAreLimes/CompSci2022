
#config varbles
user_attempts = 5 
pass_attempts = 3

def getUserName():

    """get the user input and check it aganst the database if the username is admin, request the user to enter a PGP key"""

    database = [
        {'username':'a', 'pass':'123'},
        {'username':'b', 'pass':'321'},
        {'username':'c', 'pass':'456'},   
        {'username':'d', 'pass':'654'},
        {'username':'e', 'pass':'789'},
        {'username':'f', 'pass':'987'},
    ]

    user_obj = None
    auth = False
    counter = 0

    while auth == False:
        counter += 1 

        input_username = input('username: ')

        #check that the user has not tried too manny usernames
        if counter >= user_attempts:
            print('TOO MANNY ATTEMPTS')
            break

        #check for the name in the database
        for i in database:
            if input_username == i['username']:
                user_obj = i
                auth = True
                continue        # i need to use this somewhere lol

        #only run this if admin (not found in standard user database)
        if input_username == 'admin':
            input('please enter pgp verification key: ')
            print("acsess deny'd")

    else:
        return user_obj


def getPassword(user_obj=None):

    """checks the input against user object selected from above """

    if user_obj == None: return

    pass_correct = False
    counter = 0

    while pass_correct == False:
        
        counter += 1
        input_pass = input("password: ")

        if counter >= pass_attempts:
            break

        elif input_pass == user_obj['pass']:
            pass_correct = True

    else:
        return pass_correct 

    return 'TOO MANNY ATTEMPTS!'

def main():

    user_obj = getUserName()
    if user_obj==None: exit() 

    auth = getPassword(user_obj)
    if auth==False: exit()
    elif auth==True: print('welcome to the system!')
    else: print('TOO MANNY ATTEMPTS!')


if __name__ == "__main__":
    main()