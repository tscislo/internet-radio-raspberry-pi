import os


class Streams():
    def __init__(self):
        ''' Constructor. '''
        self.root = "/home/pi/Music"
        self.predefinedStreams = [
            {
                "name": "Radio ZET",
                "stream": "http://n-1-11.dcs.redcdn.pl/sc/o2/Eurozet/live/audio.livx",
                "isRadio": "true"
            },
            {
                "name": "Polskie Radio 24",
                "stream": "http://stream3.polskieradio.pl:8080",
                "isRadio": "true"
            },
            {
                "name": "ZET Gold",
                "stream": "http://zgl01.cdn.eurozet.pl:8506/ZGLHIT.mp3",
                "isRadio": "true"
            },
            {
                "name": "Meloradio",
                "stream": "http://mel02.cdn.eurozet.pl:8800/mel-net.mp3",
                "isRadio": "true"
            },
            {
                "name": "Cinemix",
                "stream": "http://94.23.51.96:8001/;",
                "isRadio": "true"
            },
            {
                "name": "Soundtracks",
                "stream": "http://hi5.streamingsoundtracks.com/;",
                "isRadio": "true"
            },
            {
                "name": "James Bond 007",
                "stream": "http://stream.laut.fm/007",
                "isRadio": "true"
            },
            {
                "name": "Radio Mambo",
                "stream": "http://178.32.139.184:8060/;",
                "isRadio": "true"
            },
            {
                "name": "Salsa Warriors",
                "stream": "http://192.99.17.12:6031/;stream/1",
                "isRadio": "true"
            },
            {
                "name": "Salsa AMS",
                "stream": "http://82.94.166.107:8067/;stream/1",
                "isRadio": "true"
            },
            {
                "name": "Fox News",
                "stream": "http://streaming-ent.shoutcast.com/foxnews",
                "isRadio": "true"
            },
            {
                "name": "RFI Monde",
                "stream": "http://live02.rfi.fr/rfimonde-96k.mp3",
                "isRadio": "true"
            },
            {
                "name": "BBC 1",
                "stream": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p",
                "isRadio": "true"
            },
            {
                "name": "BBC 2",
                "stream": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p",
                "isRadio": "true"
            }
        ]

    def get(self):
        for root, dirs, files in os.walk(self.root):
            if len(dirs):
                extraStreams = []
                for dir in dirs:
                    extraStreams.append({"name": dir, "stream": self.root + "/" + dir, "isRadio": "false"})
                allStreams = extraStreams + self.predefinedStreams
                allStreams.sort(key=lambda stream: (stream["isRadio"], stream["name"]), reverse=False)
                return allStreams
            else:
                return self.predefinedStreams
