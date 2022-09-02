import time
from mutagen.mp3 import MP3

import subprocess as sp
import os
import signal

import keyboard
# import psutil


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


def player(command=None):

    #audio data
    audio_path = 'C:/Users/User/Downloads/TEST.mp3'
    audio_len = MP3(audio_path).info.length

    #playback data
    start_time = 0
    playback_time = 0

    #prevents multiple songs from playing
    is_playing = False

    if command == 'play' and is_playing == False: 
        #play audio
        pid = play(audio_path, playback_time)
        is_playing = True
    
    elif command == 'pause' and is_playing == True:
        exit(pid)
        is_playing = False
  
    else:
        print('something went wrong')



def prog_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '=' * int(percent) + '-' * (100 - int(percent))
    print(f'\r|{bar}|', end='\r')

def start_prog_bar(audio_len, playback_time):
    while True:
        prog_bar(playback_time, audio_len)




#     # https://stackoverflow.com/questions/8135899/how-to-detect-if-a-process-is-running-using-python-on-win-and-mac

def detect_input():
    #audio data
    audio_path = 'C:/Users/User/Downloads/TEST.mp3'
    audio_len = MP3(audio_path).info.length

    pause_toggale = False
    is_pressing = False

    start_time = 0
    playback_time = 0

    if is_pressing != True:
        is_pressing = True
        keypress = keyboard.read_key()

        if keypress == 'space':  
            if pause_toggale == False:   
                player('play')

                start_time = time.perf_counter()
                is_playing = True
                pause_toggale = True
            
            elif pause_toggale == True:
                player('pause')

                playback_time += time.perf_counter() - start_time
                is_playing = False   
                pause_toggale = False   
            
    else:
        time.sleep(1)
        is_pressing = False


while True:
    detect_input()
    print('iter')