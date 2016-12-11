import sys, os, subprocess
from subprocess import check_output
from threading import Thread
from time import sleep
import time
from statusThread import StatusThread
from radioControl import RadioControl

print('Internet Radio started!')
subprocess.Popen(['mocp', '-a', './streams/all.m3u', '-c'])

if __name__ == "__main__":
    radioControl = RadioControl()
    statusThread = StatusThread()
    statusThread.start()
    radioControl.statusThread = statusThread
    while True:
        time.sleep(7)
        radioControl.next()