import json

from tools.key_mgmt import encrypt_json, return_json


encrypt_json()
json_object = json.loads(return_json())
print(str(json_object["API Key"]))
get_date()

