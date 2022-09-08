import TA_module1 as user_db
import pages

input_name = input("enter a username: ")


#check if the name exists
if user_db.check_name_exist(input_name):

    #if it does, ask for password
    print('user found')
    password = input("enter the password: ")

    #check if the password is correct
    if user_db.auth(input_name, password):
        
        while True:
            pages.homepage()

    else:
        print('password incorrect') 

else:
    print('user not found!')



