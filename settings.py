import json
import os

dir_path = os.path.dirname(os.path.abspath(__file__))


class Settings():
    def __init__(self):
        self.loadedJson = None
        with open(dir_path + '/settings/settings.json', 'r') as settingsFile:
            self.loadedJson = json.load(settingsFile)

    def get(self):
        if self.loadedJson:
            return self.loadedJson
        else:
            return None

    def set(self, settings):
        with open(dir_path + '/settings/settings.json', 'w') as settingsFile:
            json.dump(settings, settingsFile)
