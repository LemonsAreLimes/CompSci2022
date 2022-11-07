import turtle
import time 
import random

def login():

    """this function is the inital login screen"""

    #print welcome message
    print('welcome to TurtleBox!')
    print('written by - LemonsAreLimes')
    print()
    time.sleep(0.5)
    print('to play this game you need to login....')

    #define the database
    db = [
        {'name':'lemons', 'pass':'limes'},
        {'name':'are', 'pass':'r'},
        {'name':'limes', 'pass':'lemons'},
        {'name':'admin', 'pass':'password'},
        {'name':'root', 'pass':'please input a password'},
        {'name':'sudo rm -rf', 'pass':'noooo'},
        {'name':'password', 'pass':'username'},
    ]

    for n in range(5):

        if n>=1:
            print(f'attempt: {n}')
            print()

        #ask the user for the username and password
        username = input('username: ')
        password = input('password: ')

        #search db for username
        for i in db:
            if i['name'] == username:
                if i['pass'] == password:
                    return i
                else:
                    print('password is incorrect!')
        
        print('user not found!')
    
    print('you attempted too manny times!')
    print('please wait 30 years to try this game again')
    time.sleep(933120000)
    
def getPlayers():

    while True:
        player_count_temp = input('how manny people will be playing: ')
         
        #check if the user put in a number
        try:
            player_count = int(player_count_temp)

            if player_count >= 10:
                print('too manny players! the max is 10')
                continue
            elif player_count >=100:
                print('are you trying to explode our servers? the max is 10!')
                continue

            print()

            #get each players color and name
            player_data = []
            for i in range(player_count):

                name = input(f'player {i} name: ')

                test_color = turtle.Turtle()

                while True:
                    color = input(f'player {i} color: ')

                    #make sure the inupt is a color that will work with turtles
                    try:
                        test_color.color(color)
                        break

                    except:
                        print('color not recognized!')
                        continue

                player_data.append({ "name":name, "color":color })

            return player_data
        
        except: 
            print('input must be a number! example: 10')
            continue

def getConfig():

    #define stuff
    default_settings = {
        "name":"DEFAULT",
        "init":{
            "size":500,
            "box_size":250,
            "speed":5,
            "pen_size":1,
            
        },
        "turtles":{
            "rnd_mv":False,
            "rnd_mv_dist_min":0,
            "rnd_mv_dist_max":100,
            "fxt_mv_dist":100,
            
            "rnd_rot_min":0,
            "rnd_rot_max":360,
            "rnd_rot_indx_ammt":45,
        }
    }

    useCustomPreset = input('would you like to use a preset? (y/n) ')

    if useCustomPreset == 'y':
        
        #define the list of presets
        presets = [
            {"name":"angular",
            "init":{
                "size":500,
                "box_size":250,
                "speed":3,
                "pen_size":4,
                },
            "turtles":{
                "rnd_mv":False,
                "rnd_mv_dist_min":0,
                "rnd_mv_dist_max":100,
                "fxt_mv_dist":75,
                
                "rnd_rot_min":-45,
                "rnd_rot_max":45,
                "rnd_rot_indx_ammt":45,}
            },
            {"name":"messy",
            "init":{
                "size":500,
                "box_size":250,
                "speed":10,
                "pen_size":1,
                },
            "turtles":{
                "rnd_mv":True,
                "rnd_mv_dist_min":0,
                "rnd_mv_dist_max":10,
                "fxt_mv_dist":100,
                
                "rnd_rot_min":0,
                "rnd_rot_max":180,
                "rnd_rot_indx_ammt":1,}
            },
            {"name":"ants",
            "init":{
                "size":500,
                "box_size":250,
                "speed":5,
                "pen_size":1,
                },
            "turtles":{
                "rnd_mv":False,
                "rnd_mv_dist_min":0,
                "rnd_mv_dist_max":100,
                "fxt_mv_dist":50,
                
                "rnd_rot_min":0,
                "rnd_rot_max":360,
                "rnd_rot_indx_ammt":90,}
            },
            {"name":"quick match",
            "init":{
                "size":500,
                "box_size":250,
                "speed":10,
                "pen_size":1,
                },
            "turtles":{
                "rnd_mv":False,
                "rnd_mv_dist_min":0,
                "rnd_mv_dist_max":100,
                "fxt_mv_dist":150,
                
                "rnd_rot_min":0,
                "rnd_rot_max":360,
                "rnd_rot_indx_ammt":1,}
            },
            {"name":"idk just try it out",
            "init":{
                "size":500,
                "box_size":250,
                "speed":5,
                "pen_size":10,
                },
            "turtles":{
                "rnd_mv":True,
                "rnd_mv_dist_min":0,
                "rnd_mv_dist_max":100,
                "fxt_mv_dist":0,
                
                "rnd_rot_min":0,
                "rnd_rot_max":360,
                "rnd_rot_indx_ammt":1,}
            }
        ]

        #print out all the presets
        print('PRESETS:')
        print('0: exit')
        for i in range(len(presets)):
            print(f"{i+1}: {presets[i]['name']}")

        while True:

            #get the input
            print()
            chosen_set = input('enter in the preset number cooresponding to the one you want to use: ')

            if chosen_set == '0':
                print('using default settings...')
                return default_settings
            else:

                try:
                    return presets[int(chosen_set)-1]
                except:
                    print('invalid input!')
                    continue

    else:
        return default_settings

def run_game(players=None, game_data=None):
    if players==None: return "PERAM ERR!!!!"

    #init the window
    window = turtle.Screen()
    window.clear()
    turtle.speed(game_data['init']['speed'])
    bx_size = game_data['init']['box_size']

    #init the square
    t = turtle.Turtle()
    t.penup()
    t.goto(-bx_size,-bx_size)
    t.pendown()
    t.goto(-bx_size,bx_size)
    t.goto(bx_size,bx_size)
    t.goto(bx_size,-bx_size)
    t.goto(-bx_size,-bx_size)

    #initialize the list of turtles
    sea_turtles = []
    for i in players:
        t = turtle.Turtle()
        t.color(i['color'])
        t.speed(game_data['init']['speed'])

        sea_turtles.append(t)

    #start the game
    winner = ''
    while True:
        
        #check if anyone has won evrey tick
        for n in range(len(sea_turtles)):

            isOutsideXrange = sea_turtles[n].xcor() > bx_size or sea_turtles[n].xcor() < -bx_size 
            isOutsideYrange = sea_turtles[n].ycor() > bx_size or sea_turtles[n].ycor() < -bx_size 

            if isOutsideXrange or isOutsideYrange:
                winner_name = players[n]['name']
                win = sea_turtles[n]
                win.penup()
                win.goto(0,0)
                win.write(f'{winner_name} is the winner!', font=("Verdana", 15, "normal"), align="center")
                winner = winner_name

        #if someone has won, exit the main loop
        if winner != '':
            time.sleep(3)
            return winner

        #move the players evrey tick
        for n in sea_turtles:

            #rotate
            n.lt(random.randrange(game_data['turtles']['rnd_rot_min'], game_data['turtles']['rnd_rot_max'], game_data['turtles']['rnd_rot_indx_ammt']))

            #move
            if game_data['turtles']['rnd_mv'] == True:
                n.fd(random.randrange(game_data['turtles']['rnd_mv_dist_min'], game_data['turtles']['rnd_mv_dist_max']))
            else:
                n.fd(game_data['turtles']['fxt_mv_dist'])

    window.exitonclick()

def main():

    login()
    print()
    user_data = getPlayers() 
    print()
    game_data = getConfig()
    print()

    counter = 0

    while True:
        counter += 1
        winner = run_game(user_data, game_data)

        print(f'the winner is: {winner}')
        play_again = input('yould you like to play again? (y/n): ')

        if play_again == 'y':
            print(f'round: {counter}')
            continue
        else:
            print()
            print('goodbye')
            print()
            exit()


    # "documentation"

    # login
        #print welcome message
        #define the database
        #ask the user for the username and password
        #search db for username

    # getPlayers
        #ask how manny players
        #check if the user put in a number
        #get each players color and name
    
    # getConfig
        #define stuff
        #define the list of presets
        #print out all the presets
        #get the input
        #return the preset

    # run_game
        #init the window
        #clear it
        #draw the square
        #initialize the list of turtles
        #start the game
        #check if anyone has won evrey tick
            #if someone has won, exit the main loop
            #ask if they want to play again
        #move the players evrey tick
            #rotate
            #move



if __name__ == "__main__":
    main()