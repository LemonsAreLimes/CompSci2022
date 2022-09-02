import keyboard
import time

from files.player import Player 
from CONFIG.config import config

command_mode = False

is_playing = False
is_pressing = False

while True:

    if is_pressing != True:
        if command_mode == False:

            is_pressing = True
            keypress = keyboard.read_key()
            if keypress == 'space':
                
                if is_playing == False:
                    Player.play()
                    is_playing = True
                
                else: 
                    Player.pause()
                    is_playing = False

            elif keypress == 'right':
                pass

            elif keypress == 'left':
                pass

            elif keypress == ':':
                command_mode = True
                pass

        if command_mode == True:
            exit()

        else:
            print(keypress)

    else:
        time.sleep(1)
        is_pressing = False