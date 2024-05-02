""" This module contains encryption and decryption related methods """
import os
import shutil

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from helper import load_encryption_key

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_DIR = os.path.join(ROOT_DIR, "key")

class FolderEncryption:
    def __init__(self, data_folder_path, key, file_encryption_format=".dat",
                 zip_format="zip", chunk_size=64):
        self.data_folder_path = data_folder_path
        self.key = key
        self.file_encryption_format = file_encryption_format
        self.zip_format = zip_format
        self.file_path = self.data_folder_path + "." + self.zip_format
        self.chunk_size = chunk_size * 1024
        self.encrypted_data_folder_path = self.file_path + self.file_encryption_format


    def encrypted_data_file_exists(self):
        if os.path.exists(self.encrypted_data_folder_path):
            return True
        return False

    def zip_folder(self, folder_path):
        shutil.make_archive(base_name=folder_path, format=self.zip_format, root_dir=folder_path)
        return folder_path + "." + self.zip_format

    def unzip_folder(self, zip_folder_path, format="zip"):
        os.makedirs(self.data_folder_path, exist_ok=True)
        shutil.unpack_archive(filename=zip_folder_path, extract_dir=self.data_folder_path, format=format)
        return self.data_folder_path

    def encrypt_file(self):
        """
        Used for file encryption
        :return: Encrypted file path
        """
        self.file_path = self.zip_folder(self.data_folder_path)
        output_file = self.file_path + self.file_encryption_format

        iv = get_random_bytes(16)
        print("self.key :: ", self.key)
        print("TYPE self.key :: ", type(self.key))
        
        print("IV :: ", iv)
        encryptor = AES.new(self.key, AES.MODE_CBC, iv)

        file_size = os.path.getsize(self.file_path)

        with open(self.file_path, 'rb') as infile:
            with open(output_file, 'wb') as outfile:
                outfile.write(iv)
                while True:
                    chunk = infile.read(self.chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    outfile.write(encryptor.encrypt(chunk))

        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        shutil.rmtree(self.data_folder_path)
        # shutil.rmtree(self.file_path)
        return output_file

    def decrypt_file(self, encrypted_file):
        """
        Used to decrypt the encrypted file
        :param encrypted_file: encrypted file path
        :return:
        """

        folder_path = os.path.dirname(encrypted_file)
        filename = os.path.basename(encrypted_file)

        file_name_without_extension, file_extension = os.path.splitext(filename)

        output_file = os.path.join(folder_path, file_name_without_extension)

        with open(encrypted_file, 'rb') as infile:
            iv = infile.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, iv)

            with open(output_file, 'wb') as outfile:
                while True:
                    chunk = infile.read(self.chunk_size)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))
        self.unzip_folder(output_file)
        return output_file


def encryption_decryption_arguments(data_directory):
    def encryption_decryption(func):
        encryption_key = load_encryption_key()
        encryption_obj = FolderEncryption(data_directory, key=encryption_key)

        def wrapper(*args, **kwargs):
            encrypted_file = encryption_obj.file_path + encryption_obj.file_encryption_format
            if not encryption_obj.encrypted_data_file_exists():
                encrypted_file = encryption_obj.encrypt_file()

            encryption_obj.decrypt_file(encrypted_file)
            print("Decrypted file")
            print("Function '{}' is running".format(func.__name__))
            func(*args, **kwargs)
            e = encryption_obj.encrypt_file()
            print("Encrypted file again")
        return wrapper
    return encryption_decryption

