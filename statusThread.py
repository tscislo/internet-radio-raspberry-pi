from threading import Thread
import time
from subprocess import check_output


class StatusThread(Thread):
    def __init__(self):
        ''' Constructor. '''

        Thread.__init__(self)

    def run(self):
        while(True):
            self.getPlaybackState(self)
            time.sleep(3)

    def getState(self):
        splittedStateJSON = {}
        try:
            state = check_output(['mocp', '--info'])
            splittedState = state.split('\n')
            for splittedStateItem in splittedState:
                if splittedStateItem != "":
                    splittedStateJSON[splittedStateItem.split(':')[0]] = splittedStateItem.split(':')[1].strip(
                        ' \t\n\r')
        except:
            splittedStateJSON['Error'] = 'Internet radio playback error!'
            pass
        return splittedStateJSON


    def getPlaybackState(self, thread):
        print '\n---------------------------'
        print 'Internet radio status checking...'
        mocpState = self.getState()
        if 'Error' in mocpState:
            print mocpState['Error']
        if 'State' in mocpState:
            print 'State: ' + mocpState['State']
        if 'Title' in mocpState:
            print 'Playing... ' + mocpState['Title']