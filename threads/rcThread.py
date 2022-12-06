from threading import Thread
from piir.io import receive
from piir.decode import decode
from piir.prettify import prettify

from gpioRCKeyMap import gpioRCKeyMap
import time


class RCThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.radioControl = None
        self.standByThread = None
        self.piFaceThread = None

    def handleRC(self):
        data = decode(receive(23))
        if data:
            keys = {'keyname': data}
            keyname = prettify(keys)['keys']['keyname']
            mappedToAction = gpioRCKeyMap.get(keyname)
            if mappedToAction:
                if mappedToAction == 'on_off':
                    self.piFaceThread.enableDisable()
                elif self.standByThread.isDisabled() and getattr(self.radioControl, mappedToAction):
                    getattr(self.radioControl, mappedToAction)()

    def run(self):
        while True:
            self.handleRC()
            time.sleep(0.1)
