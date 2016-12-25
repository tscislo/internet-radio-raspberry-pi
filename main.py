import subprocess

from threads.statusThread import StatusThread
from settings import Settings
from radioControl import RadioControl
from threads.piFaceThread import PiFaceThread

if __name__ == "__main__":
    print('Internet radio starting...')
    subprocess.Popen(['mocp', '--clear'])
    subprocess.Popen(['mocp', '--stop'])
    radioControl = RadioControl()
    statusThread = StatusThread()
    piFaceThread = PiFaceThread()
    settings = Settings()
    piFaceThread.radioControl = radioControl
    piFaceThread.settings = settings
    statusThread.piFaceThread = piFaceThread
    radioControl.statusThread = statusThread
    radioControl.piFaceThread = piFaceThread
    statusThread.radioControl = radioControl
    piFaceThread.start()
    piFaceThread.processSettings()
    statusThread.start()
    piFaceThread.enableBacklight()
    print('Internet radio started...')
