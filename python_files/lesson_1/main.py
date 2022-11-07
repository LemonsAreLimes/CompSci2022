import database_api as db
from colorama import Fore
#lemons_are_limes compsci 2022/9/7 - 2022/9/8

#display welcome message
print('''

welcome to ye olde village newfangled virtual phonebook.
"top notch security and 100% reliable" - billy joe bob.

yes my phone number is in here stop asking about it
no carol i dont have your butter now the whole village knows i dont have your damnn butter.

all you need to do is type in anythin like a name, adress, number or something random and this 
magical program show you all information you could possibly know!

''')


user_list = None              #changes from data req to query
has_seen_more_data_text = False     #prints out explainer text on data req

#main loop, allows user to request more data
while True:

    #check if a number is selected
    if user_list != None:

        #use current number for more data / display data
        explainer_text = '''
            for more data select a thing:
                0: view all data
                1: view tags
                3: create new query
                q: quit
            '''

        #check if the user has seen the prompt already -> prevents repeitiveness
        if has_seen_more_data_text == False:
            has_seen_more_data_text = True
            print(explainer_text)

        #get input for data 
        data_command = input('please select the data entry to display, or type sh to dispay selctor: ')


        if data_command == '0':    #display all the data
            print()
            for entry in user_list:
                
                print(f'Number: {entry["formatted-number"]}')
                print(f'Name: {entry["name"]}')
                print(f'Description: {entry["desc"]}')
                print(f'Adress: {entry["address"]}')
                print(f'type: {entry["type"]}')
                print()
        
        elif data_command == '1':    #display tags
            print()
            for entry in user_list:
                
                tags = ''  #stringify dict
                for tag in entry["tags"]:
                    tags += tag + " "

                print()
                print(f'tags for number {entry["formatted-number"]}')
                print(tags.replace(' ', ', '))
                print()


        elif data_command == '3':  #allow user to create a new query
            user_list = None            
            print()
            print(f'{Fore.GREEN}you can now select a new number{Fore.RESET}')
            print(f'{Fore.GREEN}-------------------------------{Fore.RESET}')
            print()

        elif data_command == 'sh': #display the explainer text
            print(explainer_text)  

        elif data_command =='q':
            print('quitting...')
            exit()

        else:                   #if the input is invalid
            print()
            print(f' {Fore.RED}input was not recognized!{Fore.RESET}')
            print('please try again')
            print()




    else:   #slected number == none

        #get user request
        query = input('please input the search query: ')

        #carry out the request
        data = db.search(query)

        #check data is valid before displaying
        if data == []:
            print(f' {Fore.RED} nothing was found for: {query}{Fore.RESET}')
            print()

        else:
            user_list = data        #set as selected number for data extraction
        
