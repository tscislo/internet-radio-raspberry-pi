from threading import Thread
import time
from subprocess import check_output


class StatusThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        self.state = "INIT"
        self.piFaceThread=""
        Thread.__init__(self)
        # self.daemon = True

    def run(self):
        print('StatusThread')
        while (True):
            self.getPlaybackState()
            time.sleep(1)

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
        # if self.state:
        #     print(self.state)
        if 'Title' in mocpState:
            msg = ' Playing... ' + mocpState['Title']
            #print(msg)
            self.piFaceThread.clear()
            self.piFaceThread.write(msg, 0)
