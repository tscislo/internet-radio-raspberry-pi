from threading import Thread
import time


class SimulateThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.daemon = True
        self.radioControl=""
        self.count = 0

    def run(self):
        print('start SimulateThread')
        while self.count <= 29:
            time.sleep(10)
            self.count += 1
            self.radioControl.previous()


