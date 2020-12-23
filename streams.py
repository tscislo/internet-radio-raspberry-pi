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
                "name": "Elton John",
                "stream": "http://streaming.exclusive.radio/er/eltonjohn/icecast.audio",
                "isRadio": True
            },
            {
                "name": "Madonna Radio",
                "stream": "http://streaming.exclusive.radio/er/madonna/icecast.audio",
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
                "name": "Christmas 1",
                "stream": "http://node-05.zeno.fm/aae9yc3ygnruv?rj-ttl=5&rj-tok=AAABdo8S4DcAoTqG00pxZjP_MQ",
                "isRadio": True
            },
            {
                "name": "Christmas 2",
                "stream": "http://str2b.openstream.co/1312?aw_0_1st.collectionid=4427&stationId=4427&publisherId=1336&k=1608717935",
                "isRadio": True
            },
            {
                "name": "Christmas 3",
                "stream": "http://tuner.m1.fm/M1-XMAS.mp3",
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
