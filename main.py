import subprocess

from threads.simulateThread import SimulateThread
from threads.statusThread import StatusThread

from radioControl import RadioControl
from threads.piFaceThread import PiFaceThread

if __name__ == "__main__":
    initialMsg = "Internet Radio..."
    print(initialMsg)
    subprocess.Popen(['mocp', '-c'])
    subprocess.Popen(['mocp', '--stop'])
    radioControl = RadioControl()
    statusThread = StatusThread()
    piFaceThread = PiFaceThread()
    piFaceThread.piFaceSwitchesThread.radioControl = radioControl
    statusThread.piFaceThread = piFaceThread
    simulateThread = SimulateThread()
    radioControl.statusThread = statusThread
    radioControl.piFaceThread = piFaceThread
    simulateThread.radioControl = radioControl
    statusThread.radioControl = radioControl
    piFaceThread.start()
    piFaceThread.write(initialMsg, 0)
    # simulateThread.start()
