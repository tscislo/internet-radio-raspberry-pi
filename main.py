import sys, os, subprocess
from statusThread import StatusThread
from radioControl import RadioControl
from piFaceThread import PiFaceThread
from simulateThread import SimulateThread

if __name__ == "__main__":
    initialMsg = "Internet Radio..."
    print(initialMsg)
    subprocess.Popen(['mocp', '-a', './streams/all.m3u', '-c'])
    radioControl = RadioControl()
    statusThread = StatusThread()
    piFaceThread = PiFaceThread()
    simulateThread = SimulateThread()
    statusThread.piFaceThread = piFaceThread
    radioControl.statusThread = statusThread
    simulateThread.radioControl = radioControl
    simulateThread.start()
    statusThread.start()
    piFaceThread.start()
    piFaceThread.write(initialMsg, 1)
    # statusThread.join()
    # piFaceThread.join()
    # simulateThread.join()
