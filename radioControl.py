import subprocess
from stationsList import stationsList

class RadioControl():
    def __init__(self):
        ''' Constructor. '''
        self.statusThread = None
        self.piFaceThread = None
        self.stationIdx = 0

    def getNextListItem(self):
        if self.stationIdx >= len(stationsList) - 1:
            self.stationIdx = 0
        else:
            self.stationIdx += 1
        return stationsList[self.stationIdx]

    def getPrevListItem(self):
        if self.stationIdx == 0:
            self.stationIdx = len(stationsList) - 1
        else:
            self.stationIdx -= 1
        return stationsList[self.stationIdx]

    def getCurrentListItem(self):
        return stationsList[self.stationIdx]

    def play_pause(self):
        self.piFaceThread.enableBacklight()
        if self.statusThread.playbackState == 'PLAY':
            self.pause()
        if self.statusThread.playbackState == 'PAUSE' or self.statusThread.playbackState == 'STOP':
            self.play()

    def play(self):
        print('Playing...')
        subprocess.Popen(['mocp', '-a', self.getCurrentListItem()['stream'], '-c', '-p'])
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PLAY'})

    def pause(self):
        print('Pausing...')
        subprocess.Popen(['mocp', '--pause'], shell=False)
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PAUSE'})

    def next(self):
        self.piFaceThread.enableBacklight()
        nextListItem = self.getNextListItem()
        print('Next... ' + nextListItem['name'])
        subprocess.Popen(['mocp', '--stop'], shell=False)
        subprocess.Popen(['mocp', '--clear'], shell=False)
        subprocess.Popen(['mocp', '-a', nextListItem['stream'], '-c', '-p'])
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PLAY'})
        self.piFaceThread.writeSecondLine("Loading...")

    def previous(self):
        self.piFaceThread.enableBacklight()
        prevListItem = self.getPrevListItem()
        print('Previous... ' + prevListItem['name'])
        subprocess.Popen(['mocp', '--stop'], shell=False)
        subprocess.Popen(['mocp', '--clear'], shell=False)
        subprocess.Popen(['mocp', '-a', prevListItem['stream'], '-c', '-p'])
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PLAY'})
        self.piFaceThread.writeSecondLine("Loading...")
