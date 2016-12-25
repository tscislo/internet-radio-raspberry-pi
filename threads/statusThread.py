from threading import Thread
import time
from subprocess import check_output
from piFaceBitmaps import bitmaps


class StatusThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        self.state = "STOP"
        self.radioControl = None
        Thread.__init__(self)
        self.daemon = True

    def run(self):
        while (True):
            self.getPlaybackState()
            time.sleep(0.2)

    def getState(self):
        splittedStateJSON = {}
        try:
            state = check_output(['mocp', '--info']).decode("utf-8")
            splittedState = state.split('\n')
            for splittedStateItem in splittedState:
                if splittedStateItem != "":
                    splittedStateJSON[splittedStateItem.split(':')[0]] = splittedStateItem.split(':')[1].strip(
                        ' \t\n\r')
        except:
            splittedStateJSON['Error'] = 'Unknown playback error!'
            pass
        return splittedStateJSON

    def getPlaybackState(self):
        mocpState = self.getState()
        if 'Error' in mocpState:
            self.state = "ERROR"
        if 'State' in mocpState:
            self.state = mocpState['State']
        if 'Title' in mocpState and mocpState['Title'] != "":
            self.piFaceThread.writeSecondLine(mocpState['Title'])
        else:
            self.piFaceThread.writeSecondLine(" ")
        if self.state:
            self.piFaceThread.writeFirstLine(bitmaps[self.state]['idx'], self.radioControl.getCurrentListItem()['name'])
