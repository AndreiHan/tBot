import json

from tools import twitter_connect
from tools.file_mgmt import init_status, check_status
from tools.key_mgmt import encrypt_json, return_json

import sys

# sys.stdout = open('logfile.txt', 'w')

encrypt_json()
check_status()
twitter_connect.send()
