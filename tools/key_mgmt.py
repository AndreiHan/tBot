import json
import os.path
from os import path

from cryptography.fernet import Fernet


def return_json():
    # Getting the key
    with open('storage/key.key', 'rb') as file:
        key = file.read()

    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('storage/KEY-e.json', 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    return fernet.decrypt(encrypted)


def create_json():
    status = \
        {
            "INIT": "True",
            "API_Key": "abcdabcdabcdabcd",
            "API_Key_Secret": "1332Q4TERWHTSHRJEUHTF",
            "ACCESS_TOKEN": "1AEWERGFVDZFER",
            "ACCESS_SECRET": "AFEWVDFGBDTGR"
        }

    credentials = ["API_Key", "API_Key_Secret", "ACCESS_TOKEN", "ACCESS_SECRET"]
    print("Starting import ... \n \n")

    for key in credentials:
        info = str(input('Enter your ' + key + "  :"))
        status[key] = info

    json_object = json.dumps(status, indent=4)

    # Writing to sample.json
    with open("storage/KEY.json", "w") as outfile:
        outfile.write(json_object)
        print("\nCreated KEY.json\n")
        outfile.close()


def encrypt_json():
    key_path = "storage/KEY.json"
    secret_key_path = "storage/key.key"
    encrypted_path = "storage/KEY-e.json"
    if path.exists(key_path):
        try:
            # this generates a key and opens a file 'key.key' and writes the key there
            key = Fernet.generate_key()
            with open(secret_key_path, 'wb') as file:
                file.write(key)
                file.close()
            # this just opens your 'key.key' and assings the key stored there as 'key'
            with open(secret_key_path, 'rb') as file:
                key = file.read()
                file.close()
            # this opens your json and reads its data into a new variable called 'data'
            with open(key_path, 'rb') as f:
                data = f.read()
                f.close()
                os.remove(key_path)
            # this encrypts the data read from your json and stores it in 'encrypted'
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)

            # this writes your new, encrypted data into a new JSON file
            with open(encrypted_path, 'wb') as f:
                f.write(encrypted)
                f.close()

        except FileNotFoundError:
            pass
