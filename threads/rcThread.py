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
        try:
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
            time.sleep(0.1)
        except OSError:
            print("[RCThread] unable to decode RC signals because of error with piFace")
            time.sleep(1)
        except:
            print("[RCThread] unable to decode RC signals due to other error!")
            time.sleep(1)

    def run(self):
        while True:
            self.handleRC()
