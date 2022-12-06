import subprocess

from threads.statusThread import StatusThread
from settings import Settings
from radioControl import RadioControl
from threads.piFaceThread import PiFaceThread
from threads.standbyThread import StandByThread
from threads.rcThread import RCThread

if __name__ == "__main__":
    print('Internet radio starting...')
    subprocess.Popen(['mocp', '--clear'])
    subprocess.Popen(['mocp', '--stop'])
    radioControl = RadioControl()
    statusThread = StatusThread()
    piFaceThread = PiFaceThread()
    standbyThread = StandByThread()
    rcThread = RCThread()
    rcThread.radioControl = radioControl
    rcThread.standByThread = standbyThread
    rcThread.piFaceThread = piFaceThread
    standbyThread.piFaceThread = piFaceThread
    standbyThread.statusThread = statusThread
    settings = Settings()
    piFaceThread.standbyThread = standbyThread
    piFaceThread.radioControl = radioControl
    piFaceThread.settings = settings
    statusThread.piFaceThread = piFaceThread
    radioControl.statusThread = statusThread
    radioControl.piFaceThread = piFaceThread
    statusThread.radioControl = radioControl
    piFaceThread.start()
    piFaceThread.processSettings()
    statusThread.start()
    standbyThread.start()
    rcThread.start()
    piFaceThread.enableBacklight()
    print('Internet radio started...')
