# mytimer.py
from datetime import datetime
import time

#thanks to scign on stackoverflow for writing this
#https://stackoverflow.com/users/6831393/scign
#https://stackoverflow.com/questions/60026296/how-to-make-a-pausable-timer-in-python

class MyTimer():
    """
    timer.start() - should start the timer
    timer.pause() - should pause the timer
    timer.resume() - should resume the timer
    timer.get() - should return the current time
    """

    def __init__(self):
        self.timestarted = None
        self.timepaused = None
        self.paused = False

    def start(self):
        self.timestarted = datetime.now()

    def pause(self):
        self.timepaused = datetime.now()
        self.paused = True

    def resume(self):
        pausetime = datetime.now() - self.timepaused
        self.timestarted = self.timestarted + pausetime
        self.paused = False

    def get(self):
        if self.paused:
            return self.timepaused - self.timestarted
        else:
            return datetime.now() - self.timestarted
