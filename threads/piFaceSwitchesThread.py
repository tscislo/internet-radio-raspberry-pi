from threading import Thread
import pifacecad_emulator as pifacecad
import time



class PiFaceSwitchesThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.cad = ""
        self.radioControl = ""

    def run(self):
        while True:
            self.handleSwitches()
            time.sleep(0.07)

    def handleSwitches(self):
        if self.cad.switches[0].value:
            self.radioControl.play_pause()
        if self.cad.switches[1].value:
            self.radioControl.previous()
        if self.cad.switches[2].value:
            self.radioControl.next()

