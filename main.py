import subprocess

from threads.statusThread import StatusThread

from radioControl import RadioControl
from threads.piFaceThread import PiFaceThread

if __name__ == "__main__":
    initialMsg = "Internet Radio..."
    print(initialMsg)
    subprocess.Popen(['mocp', '--clear'])
    subprocess.Popen(['mocp', '--stop'])
    radioControl = RadioControl()
    statusThread = StatusThread()
    piFaceThread = PiFaceThread()
    piFaceThread.radioControl = radioControl
    statusThread.piFaceThread = piFaceThread
    radioControl.statusThread = statusThread
    radioControl.piFaceThread = piFaceThread
    statusThread.radioControl = radioControl
    piFaceThread.start()
    piFaceThread.writeFirstLine(initialMsg)
