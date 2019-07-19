import subprocess
from streams import Streams


class RadioControl():
    def __init__(self):
        ''' Constructor. '''
        self.statusThread = None
        self.piFaceThread = None
        self.stationIdx = 0
        self.streams = Streams()

    def getNextListItem(self):
        if self.stationIdx >= len(self.streams.get()) - 1:
            self.stationIdx = 0
        else:
            self.stationIdx += 1
        return self.streams.get()[self.stationIdx]

    def getPrevListItem(self):
        if self.stationIdx == 0:
            self.stationIdx = len(self.streams.get()) - 1
        else:
            self.stationIdx -= 1
        return self.streams.get()[self.stationIdx]

    def getCurrentListItem(self):
        return self.streams.get()[self.stationIdx]

    def nextOnList(self):
        if self.getCurrentListItem()['isRadio'] == False:
            print('Next track...')
            self.piFaceThread.enableBacklight()
            subprocess.Popen(['mocp', '-f'])

    def prevOnList(self):
        if self.getCurrentListItem()['isRadio'] == False:
            print('Prev track...')
            self.piFaceThread.enableBacklight()
            subprocess.Popen(['mocp', '-r'])

    def play_pause(self, event=None):
        self.piFaceThread.enableBacklight()
        if self.statusThread.playbackState == 'PLAY':
            self.pause()
        if self.statusThread.playbackState == 'PAUSE' or self.statusThread.playbackState == 'STOP':
            self.play()

    def play(self, event=None):
        print('Playing...')
        if self.statusThread.playbackState == 'PAUSE':
            subprocess.Popen(['mocp', '--unpause'], shell=False)
        else:
            subprocess.Popen(['mocp', '-a', self.getCurrentListItem()['stream'], '-c', '-p'])
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PLAY'})

    def stop(self, event=None):
        print('Stopping...')
        subprocess.Popen(['mocp', '--stop'], shell=False)
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'STOP'})

    def pause(self, event=None):
        print('Pausing...')
        subprocess.Popen(['mocp', '--pause'], shell=False)
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PAUSE'})

    def retry_playback(self, event=None):
        self.piFaceThread.enableBacklight()
        print('Retry playback...')
        subprocess.Popen(['mocp', '--stop'], shell=False)
        subprocess.Popen(['mocp', '--clear'], shell=False)
        subprocess.Popen(['mocp', '-a', self.getCurrentListItem()['stream'], '-c', '-p'])

    def next(self, event=None):
        self.piFaceThread.enableBacklight()
        nextListItem = self.getNextListItem()
        print('Next... ' + nextListItem['name'])
        subprocess.Popen(['mocp', '--stop'], shell=False)
        subprocess.Popen(['mocp', '--clear'], shell=False)
        subprocess.Popen(['mocp', '-a', nextListItem['stream'], '-c', '-p'])
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PLAY'})
        self.piFaceThread.writeSecondLine("Loading...")

    def previous(self, event=None):
        self.piFaceThread.enableBacklight()
        prevListItem = self.getPrevListItem()
        print('Previous... ' + prevListItem['name'])
        subprocess.Popen(['mocp', '--stop'], shell=False)
        subprocess.Popen(['mocp', '--clear'], shell=False)
        subprocess.Popen(['mocp', '-a', prevListItem['stream'], '-c', '-p'])
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PLAY'})
        self.piFaceThread.writeSecondLine("Loading...")

    def volumeUp(self, event=None):
        self.piFaceThread.enableBacklight()
        subprocess.Popen(['amixer', 'set', 'PCM', '1000+'], shell=False)
        self.piFaceThread.writeSecondLine("Volume up...")

    def volumeDown(self, event=None):
        self.piFaceThread.enableBacklight()
        subprocess.Popen(['amixer', 'set', 'PCM', '1000-'], shell=False)
        self.piFaceThread.writeSecondLine("Volume down...")
