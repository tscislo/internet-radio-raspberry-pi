from threading import Thread
# Emulator
# import pifacecad_emulator as pifacecad
import pifacecad as pifacecad
import time
from threads.piFaceSwitchesThread import PiFaceSwitchesThread

cad = pifacecad.PiFaceCAD()


# PLAY_SYMBOL = pifacecad.LCDBitmap(
#     [0x10, 0x18, 0x1c, 0x1e, 0x1c, 0x18, 0x10, 0x0])
# PAUSE_SYMBOL = pifacecad.LCDBitmap(
#     [0x0, 0x1b, 0x1b, 0x1b, 0x1b, 0x1b, 0x0, 0x0])
# INFO_SYMBOL = pifacecad.LCDBitmap(
#     [0x6, 0x6, 0x0, 0x1e, 0xe, 0xe, 0xe, 0x1f])
# MUSIC_SYMBOL = pifacecad.LCDBitmap(
#     [0x2, 0x3, 0x2, 0x2, 0xe, 0x1e, 0xc, 0x0])
#
# PLAY_SYMBOL_INDEX = 0
# PAUSE_SYMBOL_INDEX = 1
# INFO_SYMBOL_INDEX = 2
# MUSIC_SYMBOL_INDEX = 3


class PiFaceThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.oldText = ""
        self.newText = ""
        self.row = 0
        self.backLightTime = 0
        self.piFaceSwitchesThread = PiFaceSwitchesThread()
        self.piFaceSwitchesThread.cad = cad
        self.piFaceSwitchesThread.start()
        cad.lcd.blink_off()
        cad.lcd.cursor_off()
        # cad.lcd.store_custom_bitmap(PLAY_SYMBOL_INDEX, PLAY_SYMBOL)
        # cad.lcd.store_custom_bitmap(PAUSE_SYMBOL_INDEX, PAUSE_SYMBOL)
        # cad.lcd.store_custom_bitmap(INFO_SYMBOL_INDEX, INFO_SYMBOL)

    def enableBacklight(self):
        self.backLightTime = 90  # backlight on for 9 sec

    def run(self):
        print('start PiFaceThread')
        self.handleKeys()
        while True:
            self.handleDisplay()
            time.sleep(0.1)

    def handleKey(self, event):
        print(str(event.pin_num))

    def handleKeys(self):
        listener = pifacecad.SwitchEventListener(chip=cad)
        for i in range(8):
            listener.register(i, pifacecad.IODIR_FALLING_EDGE, self.handleKey)
        listener.activate()

    def handleDisplay(self):
        if self.newText != self.oldText:
            cad.lcd.clear()
            cad.lcd.set_cursor(0, self.row)
            cad.lcd.write(self.newText)
            self.oldText = self.newText
        elif len(self.newText) > 16:
            cad.lcd.move_right()
        if self.backLightTime > 0:
            cad.lcd.backlight_on()
            self.backLightTime -= 1
        else:
            cad.lcd.backlight_off()

    def write(self, text, row):
        self.row = row;
        self.newText = text
