import sys, os, subprocess
from statusThread import StatusThread
from radioControl import RadioControl
from simulateThread import SimulateThread
from  piFaceThread import PiFaceThread


if __name__ == "__main__":
    initialMsg = "Internet Radio..."
    print(initialMsg)
    subprocess.Popen(['mocp', '-c'])
    subprocess.Popen(['mocp', '--stop'])
    radioControl = RadioControl()
    statusThread = StatusThread()
    piFaceThread = PiFaceThread()
    statusThread.piFaceThread = piFaceThread
    simulateThread = SimulateThread()
    radioControl.statusThread = statusThread
    simulateThread.radioControl = radioControl
    statusThread.radioControl = radioControl
    piFaceThread.start()
    piFaceThread.write(initialMsg, 0)
    simulateThread.start()
