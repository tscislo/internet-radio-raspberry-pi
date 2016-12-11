import sys, os, subprocess
from subprocess import check_output
from threading import Thread
from time import sleep
from statusThread import StatusThread

#subprocess.Popen(['mocp', '-a', './streams/all.m3u', '-c', '-p'])


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



if __name__ == "__main__":
    statusThread = StatusThread()
    statusThread.start()