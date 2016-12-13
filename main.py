import sys, os, subprocess
import time
from statusThread import StatusThread
from radioControl import RadioControl
import pifacecad_emulator as pifacecad

initialMsg = "Internet Radio loading..."
print(initialMsg)
cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.blink_off()
cad.lcd.cursor_off()
cad.lcd.write(initialMsg)
cad.lcd.move_right()
cad.lcd.move_right()
cad.lcd.move_right()
subprocess.Popen(['mocp', '-a', './streams/all.m3u', '-c'])

# if __name__ == "__main__":
#     radioControl = RadioControl()
#     statusThread = StatusThread()
#     statusThread.start()
#     radioControl.statusThread = statusThread
#     while True:
#         time.sleep(7)
#         radioControl.next()