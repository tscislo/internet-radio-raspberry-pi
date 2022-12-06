from piir.io import receive
from piir.decode import decode
from piir.prettify import prettify
import json


while True:
    data = decode(receive(23))
    keys = {}
    keys['keyname'] = data
    print(json.dumps(prettify(keys)))
