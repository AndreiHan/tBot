import json

import tweepy

from tools import twitter_message, status
from tools.get_info import get_date
from tools.key_mgmt import return_json


def send():
    api = connect()
    if api:
        text = twitter_message.get_text()
        try:
            api.update_status(text)
            print("Tweet send successfuly")
            status.set_content(text)
            status.set_time(get_date())
            return True
        except SystemExit:
            # clean-up
            raise
        except KeyboardInterrupt:
            # clean-up
            raise
        except:
            print("Tweet send failed")


def connect():
    json_object = json.loads(return_json())

    # Authenticate to Twitter

    auth = tweepy.OAuthHandler(json_object["API_Key"], json_object["API_Key_Secret"])
    auth.set_access_token(json_object["ACCESS_TOKEN"], json_object["ACCESS_SECRET"])

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        return api

    except SystemExit:
        # clean-up
        raise
    except KeyboardInterrupt:
        # clean-up
        raise
    except:
        print("Error during authentication")
