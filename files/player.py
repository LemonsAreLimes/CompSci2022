import os
import signal
import subprocess as sp
from mutagen.mp3 import MP3
import threading as th
import time

from CONFIG.config import config as c 

class Player():
    dir = c.download_dir
    playing = False
    active_pid = None

    length = MP3(dir).info.length
    start_time = 0
    playback_time = 0 

    def play():
        if Player.playing == False: 
            audio = th.Thread(target=play_audio)
            audio.start()
            print('audio is playing')
        else:
            print('audio is aready playing')

    def exit():
        if Player.exit_ffplay() == True:
            Player.playback_time = 0
            Player.start_time = 0
            print('closed ffplay')
 
    def pause():
        if Player.exit_ffplay() == True:
            Player.playback_time += (time.time() - Player.start_time)
            print('paused ffplay')

    def exit_ffplay():                  #exits ffplay, used twice to might aswell make it a seprate function
        if Player.active_pid != None and Player.playing == True:
            os.kill(int(Player.active_pid), signal.SIGTERM)
            Player.active_pid = None
            Player.playing = False
            return True
        else:
            print('ffplay already closed')



#actually plays the audio in a new thread to allow commands to keep running
def play_audio():
    command = f'ffplay -loglevel quiet -showmode 0 -i -autoexit -ss {Player.playback_time} {Player.dir}'
    audio = sp.Popen(command)

    Player.start_time = time.time()
    Player.active_pid = int(audio.pid)
    Player.playing = True

    ret = audio.wait()
    if ret == 0:
        Player.playing = False
        Player.active_pid = None

        #call the skip song function (yet to be made)


# while True:
#     x = input()
#     p = Player()

#     if x == '1':
#         p.play()
#     elif x == '2':
#         p.exit()
#     elif x == '3':
#         p.pause()
#     else:
#         print('input not recognized')