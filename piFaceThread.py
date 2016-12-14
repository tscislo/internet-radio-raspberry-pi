from threading import Thread
import pifacecad_emulator as pifacecad
import time


class PiFaceThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.daemon = True
        self.writeTextState = False
        self.cad = pifacecad.PiFaceCAD()
        self.cad.lcd.backlight_on()
        self.cad.lcd.blink_off()
        self.cad.lcd.cursor_off()

    def run(self):
        print('start PiFaceThread')

    def write(self, text, row):
        # self.cad.lcd.clear()
        self.cad.lcd.set_cursor(0, row)
        self.cad.lcd.write(text)
        self.writeTextState = True
        while self.writeTextState:
            self.cad.lcd.move_right()
            time.sleep(2)

    def clear(self):
        self.writeTextState = False
        self.cad.lcd.clear()


