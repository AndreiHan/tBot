import json


def init_status():
    create_file("storage/status.json")
    write_basic_json("storage/status.json")

def write_basic_json(path):

    status ={
        "Content" : "none",
        "Last Tweet Time" : "none"
    }

    json_object = json.dumps(status, indent=4)

    # Writing to sample.json
    with open(path, "w") as outfile:
        outfile.write(json_object)

def create_file(path):
    try:
        from pathlib import Path
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