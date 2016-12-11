import sys, os, subprocess

class RadioControl():
    def __init__(self):
        ''' Constructor. '''
        self.statusThread = ""

    def play_pause(self):
        if self.statusThread.state =='PLAY':
            print('Pausing...')
            subprocess.Popen(['mocp', '--pause'], shell=False)
        if self.statusThread.state == 'PAUSE' or self.statusThread.state == 'STOP':
            print('Playing...')
            subprocess.Popen(['mocp', '--play'], shell=False)

    def next(self):
        print('Next...')
        if self.statusThread.state == 'PLAY':
            subprocess.Popen(['mocp', '--next'], shell=False)
        else:
            subprocess.Popen(['mocp', '--play'], shell=False)

    def previous(self):
        print('Previous..')
        if self.statusThread.state == 'PLAY':
            subprocess.Popen(['mocp', '--previous'], shell=False)
        else:
            subprocess.Popen(['mocp', '--play'], shell=False)