from threading import Thread
import time
from subprocess import check_output
from piFaceBitmaps import bitmaps


class StatusThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        self.playbackState = "STOP"
        self.state = "DISABLED"
        self.radioControl = None
        Thread.__init__(self)
        self.daemon = True

    def run(self):
        while True:
            if self.state == "ENABLED":
                self.getPlaybackState()
            time.sleep(0.2)

    def getMocpState(self):
        splittedStateJSON = {}
        try:
            state = check_output(['mocp', '--info']).decode("utf-8")
            splittedState = state.split('\n')
            for splittedStateItem in splittedState:
                if splittedStateItem != "":
                    splittedStateJSON[splittedStateItem.split(':')[0]] = splittedStateItem.split(':')[1].strip(
                        ' \t\n\r')
        except:
            splittedStateJSON['Error'] = 'Some error has occurred...'
            pass
        return splittedStateJSON

    def retryLastOperation(self):
        if self.playbackState == "PLAY":
            self.radioControl.retry_playback()

    def getPlaybackState(self):
        mocpState = self.getMocpState()
        if 'Error' in mocpState:
            self.playbackState = "ERROR"
        if 'State' in mocpState:
            self.playbackState = mocpState['State']
        if 'Title' in mocpState and mocpState['Title'] != "":
            self.piFaceThread.writeSecondLine(mocpState['Title'])
        elif self.playbackState == "PLAY":
            self.piFaceThread.clearSecondLine()
        if self.playbackState:
            self.piFaceThread.writeFirstLine(bitmaps[self.playbackState]['idx'],
                                             self.radioControl.getCurrentListItem()['name'])
            if self.playbackState == "ERROR":
                self.piFaceThread.writeSecondLine(mocpState['Error'])
