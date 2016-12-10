import sys, os, subprocess
from subprocess import check_output
print "Internet Radio"



# subprocess.Popen(['mocp', '-a', './streams/all.m3u', '-c', '-p'])


# print "Playing... " + sys.argv[1]


# def play_next():
#     if (os.path.exists(os.getenv('HOME')+'/.moc/pid')):
#         print "Next"
#         subprocess.Popen(['mocp', '--next'])
#     else:
#         print "Play"
#         subprocess.Popen(['mocp', '--play'])
#
# play_next()

# subprocess.Popen(['mocp', '-a', radio_stations[sys.argv[1]], '-c', '-p'])
# subprocess.Popen(['mocp', '-i'])

def getState():
    splittedStateJSON = {}
    state = check_output(['mocp', '--info'])
    splittedState = state.split('\n')
    for splittedStateItem in splittedState:
        if splittedStateItem != "":
            splittedStateJSON[splittedStateItem.split(':')[0]] = splittedStateItem.split(':')[1].strip(' \t\n\r')
    return splittedStateJSON

print getState()['State']
