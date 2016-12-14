from threading import Thread
import pifacecad_emulator as pifacecad
import time


class SimulateThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        # self.daemon = True
        self.radioControl=""

    def run(self):
        print('start SimulateThread')
        while (True):
            time.sleep(15)
            self.radioControl.next()


