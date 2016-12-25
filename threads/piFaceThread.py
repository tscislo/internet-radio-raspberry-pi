from threading import Thread
# Emulator
# import pifacecad_emulator as pifacecad
import pifacecad as pifacecad
import time

cad = pifacecad.PiFaceCAD()


class PiFaceThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.firstLine = {'old': None, 'new': None}
        self.secondLine = {'state': None, 'radioStation': None}
        self.bitmapSymbol = None
        self.radioControl = None
        self.backLightTime = 0
        self.scrollCounter = 0
        cad.lcd.blink_off()
        cad.lcd.cursor_off()

    def enableBacklight(self):
        self.backLightTime = 100  # backlight on for 10 sec

    def run(self):
        self.handleKeys()
        while True:
            self.handleDisplay()
            self.handleBacklight()
            time.sleep(0.1)

    def handleKey(self, event):
        if event.pin_num == 0 or event.pin_num == 5:
            self.radioControl.play_pause()
        elif event.pin_num == 1 or event.pin_num == 6:
            self.radioControl.previous()
        elif event.pin_num == 2 or event.pin_num == 7:
            self.radioControl.next()

    def handleKeys(self):
        listener = pifacecad.SwitchEventListener(chip=cad)
        for i in range(8):
            listener.register(i, pifacecad.IODIR_FALLING_EDGE, self.handleKey)
        listener.activate()

    def handleBacklight(self):
        if self.backLightTime > 0:
            cad.lcd.backlight_on()
            self.backLightTime -= 1
        else:
            cad.lcd.backlight_off()

    def handleDisplay(self):
        if self.firstLine['new'] != self.firstLine['old']:
            self.scrollCounter = 0
            cad.lcd.clear()
            cad.lcd.set_cursor(0, 1)
            cad.lcd.write(self.firstLine['new'][:16])
            self.firstLine['old'] = self.firstLine['new']
        elif len(self.firstLine['new']) > 16:
            cad.lcd.set_cursor(0, 1)
            cad.lcd.write(self.firstLine['new'][self.scrollCounter:self.scrollCounter + 16])
            if self.scrollCounter == len(self.firstLine['new']):
                self.scrollCounter = 0
            else:
                self.scrollCounter += 1
        if self.secondLine['state'] != None:
            cad.lcd.set_cursor(0, 0)
            cad.lcd.write_custom_bitmap(self.secondLine['state'])
        if self.secondLine['radioStation'] != None:
            cad.lcd.set_cursor(2, 0)
            cad.lcd.write(self.secondLine['radioStation'])

    def writeSecondLine(self, text):
        self.firstLine['new'] = text + " "

    def writeFirstLine(self, state, radioStation):
        self.secondLine['state'] = state
        radioStation = radioStation[:15]
        if len(radioStation) < 14:
            diff = 14 - len(radioStation)
            for i in range(0, diff):
                radioStation += " "
        self.secondLine['radioStation'] = radioStation[:15]
