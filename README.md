# Data-Encryption-Decryption-using-AES

This repository provides a Python implementation for data encryption and decryption using the Advanced Encryption Standard (AES) algorithm.

## Features
- Encrypts and decrypts data using AES with support for common key sizes (128, 192, 256 bits).
- Offers options for key generation and storage (implementation details will be provided in the code).
- Includes the optional Initialization Vector (IV) for enhanced security in specific use cases.
- Designed to be adaptable for customization based on your project's requirements.

## Target Audience
- Developers looking to integrate secure data encryption into their applications.
- Security professionals interested in exploring the practical use of AES.
- Anyone who wants to understand and leverage AES for data security.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages from requirements.txt

```bash
git clone https://github.com/ssumitk14/Data-Encryption-Decryption-using-AES.git
```

```bash
pip install -r requirements.txt
```

## Usage

```python
import time
from folder_encryption import encryption_decryption_arguments

DATA_DIR = 'DATA_FOLDER_TO_ENCRYPT'
@encryption_decryption_arguments(DATA_DIR)
def data_processing():
    print("Data processing started")
    time.sleep(5)
    print("Data Processing finished")

if __name__ == "__main__":
    data_processing()
```


