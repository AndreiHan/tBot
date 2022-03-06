import json
import os
from pathlib import Path


# checks if status.json exists and creates it
def check_status():
    if not check_file("storage/status.json"):
        init_status()


# return True if the key exists (after app restart)
# return False is key must be imported
def check_key():
    return check_file("storage/key.key") and check_file("KEY-e.json")


def init_status():
    create_file("storage/status.json")
    write_basic_json("storage/status.json")


def write_basic_json(path):
    status = {
        "Last_Content": "none",
        "Last_Tweet_Date": "none"
    }

    json_object = json.dumps(status, indent=4)

    # Writing to sample.json
    with open(path, "w") as outfile:
        outfile.write(json_object)
        outfile.close()


def check_file(path):
    try:
        p = Path(path)
        if p.is_file() and os.path.getsize(path) > 0:
            print(path + " file exist")
            return True
        else:
            print(path + " file does not exist")
            return False
    except FileNotFoundError:
        print(path + " file does not exist")
        return False


def create_file(path):
    try:
        p = Path(path)
        if p.is_file():
            print(path + " file exist")
        else:
            print(path + " file does not exist")
            with p.open("w", encoding="utf-8") as f:
                f.write("")
                f.close()
                print(path + " file created successfully")
    except FileNotFoundError:
        print("File cannot be created")
