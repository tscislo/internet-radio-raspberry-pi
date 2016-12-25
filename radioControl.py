import sys, os, subprocess
import os

dir_path = os.path.dirname(os.path.abspath(__file__))


class RadioControl():
    def __init__(self):
        ''' Constructor. '''
        self.statusThread = None
        self.piFaceThread = None
        self.stationIdx = 0
        self.list = [
            {
                "name": "RMF Classic",
                "file": "rmf_classic.m3u"
            },
            {
                "name": "RMF Filmowa",
                "file": "rmf_muzykafilmowa.m3u"
            },
            {
                "name": "RMF 70s",
                "file": "rmf_70s.m3u"
            },
            {
                "name": "RMF 80s",
                "file": "rmf_80s.m3u"
            },
            {
                "name": "RMF Queen",
                "file": "rmf_queen.m3u"
            },
            {
                "name": "RMF Latino",
                "file": "rmf_latino.m3u"
            },
            {
                "name": "RFI Monde",
                "file": "rfi_monde.m3u"
            },
            {
                "name": "BBC 1",
                "file": "bbc1.m3u"
            },
            {
                "name": "BBC 2",
                "file": "bbc2.m3u"
            }
        ]

    def getNextListItem(self):
        if self.stationIdx >= len(self.list) - 1:
            self.stationIdx = 0
        else:
            self.stationIdx += 1
        return self.list[self.stationIdx]

    def getPrevListItem(self):
        if self.stationIdx == 0:
            self.stationIdx = len(self.list) - 1
        else:
            self.stationIdx -= 1
        return self.list[self.stationIdx]

    def getCurrentListItem(self):
        return self.list[self.stationIdx]

    def play_pause(self):
        self.piFaceThread.enableBacklight()
        if self.statusThread.state == 'PLAY':
            self.pause()
        if self.statusThread.state == 'PAUSE' or self.statusThread.state == 'STOP':
            self.play()

    def play(self):
        print('Playing...')
        subprocess.Popen(['mocp', '-a', dir_path + '/streams/' + self.getCurrentListItem()['file'], '-c', '-p'])
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
        subprocess.Popen(['mocp', '-a', dir_path + '/streams/' + nextListItem['file'], '-c', '-p'])
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PLAY'})
        self.piFaceThread.writeSecondLine("Loading...")

    def previous(self):
        self.piFaceThread.enableBacklight()
        prevListItem = self.getPrevListItem()
        print('Previous... ' + prevListItem['name'])
        subprocess.Popen(['mocp', '--stop'], shell=False)
        subprocess.Popen(['mocp', '--clear'], shell=False)
        subprocess.Popen(['mocp', '-a', dir_path + '/streams/' + prevListItem['file'], '-c', '-p'])
        self.piFaceThread.settings.set({'stationIdx': self.stationIdx, 'state': 'PLAY'})
        self.piFaceThread.writeSecondLine("Loading...")
