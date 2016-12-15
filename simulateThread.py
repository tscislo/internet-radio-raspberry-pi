from threading import Thread
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
            time.sleep(10)
            self.radioControl.next()


