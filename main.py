import os
import time
from folder_encryption import encryption_decryption_arguments

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_DIR = os.path.join(ROOT_DIR, "key")
DATA_DIR = os.path.join(ROOT_DIR, "test_folder")

@encryption_decryption_arguments(DATA_DIR)
def data_processing():
    print("Data processing started")
    time.sleep(5)
    print("Data Processing finished")


if __name__ == "__main__":
    data_processing()