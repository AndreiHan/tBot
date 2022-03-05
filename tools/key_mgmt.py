from cryptography.fernet import Fernet
import os.path
from os import path


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


def encrypt_json():
    if path.exists("storage/KEY.json"):
        try:
            # this generates a key and opens a file 'key.key' and writes the key there
            key = Fernet.generate_key()
            with open('storage/key.key', 'wb') as file:
                file.write(key)

            # this just opens your 'key.key' and assings the key stored there as 'key'
            with open('storage/key.key', 'rb') as file:
                key = file.read()

            # this opens your json and reads its data into a new variable called 'data'
            with open('storage/KEY.json', 'rb') as f:
                data = f.read()

            # this encrypts the data read from your json and stores it in 'encrypted'
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)

            # this writes your new, encrypted data into a new JSON file
            with open('storage/KEY-e.json', 'wb') as f:
                f.write(encrypted)

            os.remove('storage/KEY.json')
        except FileNotFoundError as e:
            pass
    else:
        pass
