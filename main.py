import json
from tools.get_info import get_date
from tools.key_mgmt import encrypt_json, return_json
from tools.twitter_connect import send_tweet
from tools.twitter_message import get_text

import sys
# sys.stdout = open('logfile.txt', 'w')

encrypt_json()
send_tweet()
