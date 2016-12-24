import sys, os, subprocess
import os

dir_path = os.path.dirname(os.path.abspath(__file__))


class RadioControl():
    def __init__(self):
        ''' Constructor. '''
        self.statusThread = None
        self.piFaceThread = None
        self.idx = 0
        self.list = [
            {
                "name": "RMF Classic",
                "file": "rmf_classic.m3u"
            },
            {
                "name": "RMF Muzyka Filmowa",
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
        if self.idx >= len(self.list) - 1:
            self.idx = 0
        else:
            self.idx += 1
        return self.list[self.idx]

    def getPrevListItem(self):
        if self.idx == 0:
            self.idx = len(self.list) - 1
        else:
            self.idx -= 1
        return self.list[self.idx]

    def getCurrentListItem(self):
        return self.list[self.idx]

    def startStatusThread(self):
        try:
            self.statusThread.start()
        except:
            pass

    def play_pause(self):
        self.piFaceThread.enableBacklight()
        if self.statusThread.state == 'PLAY':
            print('Pausing...')
            subprocess.Popen(['mocp', '--pause'], shell=False)
        if self.statusThread.state == 'PAUSE' or self.statusThread.state == 'STOP':
            print('Playing...')
            self.startStatusThread()
            subprocess.Popen(['mocp', '-a', dir_path + '/streams/' + self.getCurrentListItem()['file'], '-c', '-p'])

    def next(self):
        self.piFaceThread.enableBacklight()
        self.startStatusThread()
        nextListItem = self.getNextListItem()
        print('Next... ' + nextListItem['name'])
        subprocess.Popen(['mocp', '--stop'], shell=False)
        subprocess.Popen(['mocp', '--clear'], shell=False)
        subprocess.Popen(['mocp', '-a', dir_path + '/streams/' + nextListItem['file'], '-c', '-p'])

    def previous(self):
        self.piFaceThread.enableBacklight()
        self.startStatusThread()
        prevListItem = self.getPrevListItem()
        print('Previous... ' + prevListItem['name'])
        subprocess.Popen(['mocp', '--stop'], shell=False)
        subprocess.Popen(['mocp', '--clear'], shell=False)
        subprocess.Popen(['mocp', '-a', dir_path + '/streams/' + prevListItem['file'], '-c', '-p'])
