import requests
import json
import pprint
import os

from requests.api import request
from config import parseConfig, parseArgs

config = json.load(open('.config.json'))

parseConfig(config)
parseArgs(config)

head = {"User-Agent": "SkyNet", "Authorization": "token {}".format(config["token"])}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(config)
pp.pprint(head)