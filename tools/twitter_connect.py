import tweepy
import json

from tools.key_mgmt import return_json


def send_tweet():
    json_object = json.loads(return_json())

    # Authenticate to Twitter

    auth = tweepy.OAuthHandler(json_object["API_Key"], json_object["API_Key_Secret"])
    auth.set_access_token(json_object["ACCESS_TOKEN"], json_object["ACCESS_SECRET"])

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        # api.update_status("Test tweet from Tweepy Python")

    except:
        print("Error during authentication")


