import TA_module1 as user_db


def homepage():
    print('''
    0: hello world
    1: go bananas
    2: exit

    3: change password
    ''')

    command = input('>_')


    if command == '0':
        print('hello world')
        print('returning back to menu')
        print()
        print()
        return
    
    elif command == '1':
        while True:
            print('bananas')

    elif command == '2':
        exit() 

    elif command == '3':
        user_db.new_user()

    else:
        print('command not recognized')


