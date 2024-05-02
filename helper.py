import os
import json
from Crypto.Random import get_random_bytes

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_DIR = os.path.join(ROOT_DIR, "key")

def generate_and_store_encryption_key(key_file_path):
    key = get_random_bytes(16)
    key_hex = key.hex()
    key_data = {"encryption_key": key_hex}

    with open(key_file_path, 'w') as file:
        json.dump(key_data, file)


def load_encryption_key():
    key_file_path = os.path.join(KEY_DIR, "secrets.json")
    if not os.path.exists(key_file_path):
        generate_and_store_encryption_key(key_file_path)

    with open(key_file_path, 'r') as file:
        key_data = json.load(file)
    
    key_hex = key_data.get('encryption_key', None)
    if key_hex:
        key = bytes.fromhex(key_hex)
        return key
    return None
        


