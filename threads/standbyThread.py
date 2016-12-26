from threading import Thread
import time
import datetime
from piFaceBitmaps import bitmaps


class StandByThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        self.piFaceThread = None
        self.statusThread = None
        self.now = None
        self.state = "ENABLED"
        Thread.__init__(self)

    def run(self):
        while (True):
            if self.state == "ENABLED":
                self.now = datetime.datetime.now()
                self.piFaceThread.writeFirstLine(bitmaps['CLOCK']['idx'], self.now.strftime("%H:%M:%S"))
                self.piFaceThread.writeSecondLine(self.now.strftime("  %d-%m-%Y"))
            time.sleep(0.3)

    def enableDisable(self):
        if self.state == "ENABLED":
            print('Disabling standby mode...')
            self.state = "DISABLED"
            self.statusThread.state = "ENABLED"
            self.statusThread.radioControl.play()
            self.piFaceThread.clearSecondLine()
        else:
            print('Enabling standby mode...')
            self.statusThread.radioControl.pause()
            self.statusThread.state = "DISABLED"
            self.state = "ENABLED"
