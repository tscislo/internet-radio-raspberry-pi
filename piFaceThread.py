from threading import Thread
import pifacecad_emulator as pifacecad
import time

cad = pifacecad.PiFaceCAD()


class PiFaceThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.oldText = ""
        self.newText = ""
        self.row = 0
        cad.lcd.backlight_on()
        cad.lcd.blink_off()
        cad.lcd.cursor_off()

    def run(self):
        print('start PiFaceThread')
        while True:
            if self.newText != self.oldText:
                cad.lcd.clear()
                cad.lcd.set_cursor(0, self.row)
                cad.lcd.write(self.newText)
                self.oldText = self.newText
            elif len(self.newText) > 16:
                cad.lcd.move_right()
            time.sleep(0.1)

    def write(self, text, row):
        self.row = row;
        self.newText = text
