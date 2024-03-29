import os


class Streams():
    def __init__(self):
        ''' Constructor. '''
        self.root = "/home/pi/Music"
        self.predefinedStreams = [
            {
                "name": "Radio ZET",
                "stream": "http://n-1-11.dcs.redcdn.pl/sc/o2/Eurozet/live/audio.livx",
                "isRadio": True
            },
            {
                "name": "Polskie Radio 24",
                "stream": "http://stream3.polskieradio.pl:8080",
                "isRadio": True
            },
            {
                "name": "ZET Gold",
                "stream": "http://zgl01.cdn.eurozet.pl:8506/ZGLHIT.mp3",
                "isRadio": True
            },
            {
                "name": "Meloradio",
                "stream": "http://mel02.cdn.eurozet.pl:8800/mel-net.mp3",
                "isRadio": True
            },
            {
                "name": "Elton John Radio",
                "stream": "http://streaming.exclusive.radio/er/eltonjohn/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Madonna Radio",
                "stream": "http://streaming.exclusive.radio/er/madonna/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Elvis Presley Radio",
                "stream": "http://streaming.exclusive.radio/er/elvispresley/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Paul McCartney Radio",
                "stream": "http://streaming.exclusive.radio/er/paulmccartney/icecast.audio",
                "isRadio": True
            },
            {
                "name": "George Michael Radio",
                "stream": "http://streaming.exclusive.radio/er/georgemichael/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Abba Radio",
                "stream": "http://streaming.exclusive.radio/er/abba/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Coldplay Radio",
                "stream": "http://streaming.exclusive.radio/er/coldplay/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Ed Sheeran Radio",
                "stream": "http://streaming.exclusive.radio/er/edsheeran/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Johnny Cash Radio",
                "stream": "http://streaming.exclusive.radio/er/johnnycash/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Phil Collins Radio",
                "stream": "http://streaming.exclusive.radio/er/philcollins/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Scorpions Radio",
                "stream": "http://streaming.exclusive.radio/er/scorpions/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Beach Boys",
                "stream": "http://streaming.exclusive.radio/er/beachboys/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Gloria Estefan",
                "stream": "http://streaming.exclusive.radio/er/gloriaestefan/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Shakira Radio",
                "stream": "http://streaming.exclusive.radio/er/shakira/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Whitney Houston Radio",
                "stream": "http://streaming.exclusive.radio/er/whitneyhouston/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Country Radio",
                "stream": "http://icepool.silvacast.com/COUNTRY108.mp3",
                "isRadio": True
            },
            {
                "name": "Cinemix",
                "stream": "http://94.23.51.96:8001/;",
                "isRadio": True
            },
            {
                "name": "Soundtracks",
                "stream": "http://hi5.streamingsoundtracks.com/;",
                "isRadio": True
            },
            {
                "name": "James Bond 007",
                "stream": "http://stream.laut.fm/007",
                "isRadio": True
            },
            {
                "name": "Radio Mambo",
                "stream": "http://178.32.139.184:8060/;",
                "isRadio": True
            },
            {
                "name": "Salsa Warriors",
                "stream": "http://192.99.17.12:6031/;stream/1",
                "isRadio": True
            },
            {
                "name": "Salsa AMS",
                "stream": "http://82.94.166.107:8067/;stream/1",
                "isRadio": True
            },
            {
                "name": "Fox News",
                "stream": "http://streaming-ent.shoutcast.com/foxnews",
                "isRadio": True
            },
            {
                "name": "RFI Monde",
                "stream": "http://live02.rfi.fr/rfimonde-96k.mp3",
                "isRadio": True
            },
            {
                "name": "BBC 1",
                "stream": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p",
                "isRadio": True
            },
            {
                "name": "BBC 2",
                "stream": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p",
                "isRadio": True
            },
            {
                "name": "Beatles",
                "stream": "http://streaming.exclusive.radio/er/beatles/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Celine Dion",
                "stream": "http://streaming.exclusive.radio/er/celinedion/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Dire Straits",
                "stream": "http://streaming.exclusive.radio/er/direstraits/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Tears for Fears",
                "stream": "http://streaming.exclusive.radio/er/tearsforfears/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Moby",
                "stream": "http://streaming.exclusive.radio/er/moby/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Christmas 1",
                "stream": "http://node-05.zeno.fm/aae9yc3ygnruv?rj-ttl=5&rj-tok=AAABdo8S4DcAoTqG00pxZjP_MQ",
                "isRadio": True
            },
            {
                "name": "Christmas 2",
                "stream": "http://tuner.m1.fm/M1-XMAS.mp3",
                "isRadio": True
            },
            {
                "name": "Koledy 1",
                "stream": "http://31.192.216.7/KOLEDY",
                "isRadio": True
            },
            {
                "name": "Koledy 2",
                "stream": "http://zt04.cdn.eurozet.pl/ZETKOL.mp3",
                "isRadio": True
            }
        ]

    def get(self):
        for root, dirs, files in os.walk(self.root):
            if len(dirs):
                extraStreams = []
                for dir in dirs:
                    extraStreams.append({"name": dir, "stream": self.root + "/" + dir, "isRadio": False})
                allStreams = extraStreams + self.predefinedStreams
                allStreams.sort(key=lambda stream: (stream["isRadio"], stream["name"]), reverse=False)
                return allStreams
            else:
                return self.predefinedStreams
