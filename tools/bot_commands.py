import time

from tools import twitter_connect, status
from tools.file_mgmt import check_status, check_key
from tools.key_mgmt import encrypt_json


def init_check():
    if not check_key():
        encrypt_json()
    check_status()


def main_loop():
    while True:
        print("")
        print("Checking date...")
        if not status.check_date():
            init_check()
            twitter_connect.send()
        else:
            print("")
            print("Too soon...")
            time.sleep(10)
