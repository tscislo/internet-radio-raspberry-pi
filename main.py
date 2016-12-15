import sys, os, subprocess
from statusThread import StatusThread
from radioControl import RadioControl
from simulateThread import SimulateThread
from  piFaceThread import PiFaceThread


if __name__ == "__main__":
    initialMsg = "Internet Radio..."
    print(initialMsg)
    subprocess.Popen(['mocp', '-a', './streams/all.m3u', '-c'])
    radioControl = RadioControl()
    statusThread = StatusThread()
    piFaceThread = PiFaceThread()
    statusThread.piFaceThread = piFaceThread
    simulateThread = SimulateThread()
    radioControl.statusThread = statusThread
    simulateThread.radioControl = radioControl
    piFaceThread.start()
    simulateThread.start()
    statusThread.start()
    piFaceThread.write(initialMsg, 0)
