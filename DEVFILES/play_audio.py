import keyboard
import subprocess as sp
import threading as t
import os
import signal
import time


def play(file_path, start_time):
    command = f'ffplay -loglevel quiet -showmode 0 -i -ss {start_time} {file_path}'
    player = sp.Popen(command)
    return player.pid

def exit(pid):
    try:
        os.kill(pid, signal.SIGTERM)
        return 1
    except:
        return 0





keypress = keyboard.read_key()
if keypress == 'space':  
    t.Thread()
    

else:
    time.sleep(1)
    is_pressing = False


# is_playing = False
# while True:

#     print('loop')

#     if is_playing == True:
#         #display progress bar
#         pass

    
    
