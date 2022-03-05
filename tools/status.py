import json


def set_date(text):
    set_json(text, "Last_Tweet_Date")


def set_content(text):
    set_json(text, "Last_Content")


def get_content():
    return get_data("Last_Content")


def get_date():
    return get_data("Last_Tweet_Date")


def set_json(text, key):
    json_file = open("storage/status.json", "r")
    json_object = json.load(json_file)
    json_file.close()

    print("#### Json change ####")
    print("### Before ###")
    print(json_object)

    json_object[key] = text

    json_file = open("storage/status.json", "w")
    json.dump(json_object, json_file)

    print("")
    print("### After ###")
    print(text)
    print("### Json change ####")
    json_file.close()


def get_data(key):
    with open('storage/status.json', 'rb') as data:
        json_object = data.read()
        data.close()
    return json_object[key]
