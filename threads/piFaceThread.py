from threading import Thread
import pifacecad as pifacecad
import time

cad = pifacecad.PiFaceCAD()


class PiFaceThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.secondLine = {'old': None, 'new': None}
        self.firstLine = {'state': None, 'radioStation': None}
        self.bitmapSymbol = None
        self.radioControl = None
        self.standbyThread = None
        self.backLightTime = 0
        self.scrollCounter = 0
        self.settings = None
        cad.lcd.blink_off()
        cad.lcd.cursor_off()

    def handleIR(self):
        listener = pifacecad.IREventListener("internet_radio")
        listener.register('on_off', self.enableDisable)
        listener.register('next', lambda x: self.radioControl.next() if self.standbyThread.isDisabled() else "")
        listener.register('prev', lambda x: self.radioControl.previous() if self.standbyThread.isDisabled() else "")
        listener.register('play', lambda x: self.radioControl.play_pause() if self.standbyThread.isDisabled() else "")
        listener.register('stop', lambda x: self.radioControl.pause() if self.standbyThread.isDisabled() else "")
        listener.register('retry_playback', lambda x: self.radioControl.retry_playback() if self.standbyThread.isDisabled() else "")
        listener.activate()


    def enableBacklight(self):
        self.backLightTime = 100  # backlight on for 10 sec

    def run(self):
        self.handleKeys()
        self.handleIR()
        while True:
            self.handleDisplay()
            self.handleBacklight()
            time.sleep(0.1)

    def enableDisable(self, event=None):
        self.enableBacklight()
        self.standbyThread.enableDisable()

    def handleKey(self, event):
        if event.pin_num == 0 or event.pin_num == 5:
            if self.standbyThread.isDisabled():
                self.radioControl.play_pause()
        elif event.pin_num == 1:
            if self.standbyThread.isDisabled():
                self.radioControl.previous()
        elif event.pin_num == 2:
            if self.standbyThread.isDisabled():
                self.radioControl.next()
        elif event.pin_num == 6:
            if self.standbyThread.isDisabled():
                self.radioControl.volumeDown()
        elif event.pin_num == 7:
            if self.standbyThread.isDisabled():
                self.radioControl.volumeUp()
        elif event.pin_num == 4:
            self.enableDisable()

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
        if self.secondLine['new'] != self.secondLine['old']:
            self.scrollCounter = 0
            cad.lcd.clear()
            cad.lcd.set_cursor(0, 1)
            cad.lcd.write(self.secondLine['new'][:16])
            self.secondLine['old'] = self.secondLine['new']
        elif self.secondLine['new'] and len(self.secondLine['new']) > 16:
            cad.lcd.set_cursor(0, 1)
            cad.lcd.write(self.secondLine['new'][self.scrollCounter:self.scrollCounter + 16])
            if self.scrollCounter == len(self.secondLine['new']):
                self.scrollCounter = 0
            else:
                self.scrollCounter += 1
        if self.firstLine['state'] != None:
            cad.lcd.set_cursor(0, 0)
            cad.lcd.write_custom_bitmap(self.firstLine['state'])
        if self.firstLine['radioStation'] != None:
            cad.lcd.set_cursor(2, 0)
            cad.lcd.write(self.firstLine['radioStation'])

    def processSettings(self):
        settingsFromFile = self.settings.get()
        if settingsFromFile:
            self.radioControl.statusThread.playbackState = settingsFromFile['state']
            self.radioControl.stationIdx = settingsFromFile['stationIdx']
            print('Settings')
            print('stationIdx -> ' + str(settingsFromFile['stationIdx']))

    def writeSecondLine(self, text):
        self.secondLine['new'] = text + " "

    def clearSecondLine(self):
        self.secondLine['new'] = " "

    def writeFirstLine(self, state, radioStation):
        self.firstLine['state'] = state
        radioStation = radioStation[:15]
        if len(radioStation) < 14:
            diff = 14 - len(radioStation)
            for i in range(0, diff):
                radioStation += " "
        self.firstLine['radioStation'] = radioStation[:15]
