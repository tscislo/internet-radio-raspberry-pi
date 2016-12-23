from threading import Thread
import time
from subprocess import check_output


class StatusThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        self.state = "STOP"
        self.radioControl = ""
        Thread.__init__(self)
        self.daemon = True

    def run(self):
        print('StatusThread')
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
            splittedStateJSON['Error'] = 'Internet radio playback error!'
            pass
        return splittedStateJSON


    def getPlaybackState(self):
        mocpState = self.getState()
        if 'Error' in mocpState:
            self.state = "ERROR"
        if 'State' in mocpState:
            self.state = mocpState['State']
        if 'Title' in mocpState and mocpState['Title'] != "":
            self.piFaceThread.write(self.radioControl.getCurrentListItem()['name'] + ' - ' + mocpState['Title'], 0)
        else:
            self.piFaceThread.write(self.radioControl.getCurrentListItem()['name'], 0)

