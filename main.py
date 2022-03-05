import json
from tools.get_info import get_rate, get_date
from tools.key_mgmt import encrypt_json, return_json
from tools.twitter_message import get_text

encrypt_json()
json_object = json.loads(return_json())
print(str(json_object["API Key"]))
get_date()

print(get_text())
