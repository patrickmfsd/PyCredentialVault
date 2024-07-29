import base64
import os
import getpass

# pip packages
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


MPASS_FILE = 'masterpw.text'

# File to store credentials
CREDENTIALS_FILE = 'credentials.txt'


# Create key from the password and salt using PBKDF2HMAC
def create_key(password: str, salt: bytes) -> bytes:
    # Convert password to bytes
    password_bytes = password.encode('utf-8')

    # Use PBKDF2HMAC to derive a key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))

    return key

def encrypt_file():
    """Encrypt the contents of CREDENTIALS_FILE using the master password from MPASS_FILE."""
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"File {CREDENTIALS_FILE} does not exist.")
        return

    password = load_master_password()

    salt = os.urandom(16)
    key = create_key(password, salt)
    fernet = Fernet(key)

    try:
        with open(CREDENTIALS_FILE, 'rb') as file:
            data = file.read()
    except IOError as e:
        print(f"Error reading file {CREDENTIALS_FILE}: {e}")
        return

    encrypted_data = fernet.encrypt(data)

    try:
        with open(CREDENTIALS_FILE, 'wb') as file:
            file.write(salt + b'\n' + encrypted_data)
    except IOError as e:
        print(f"Error writing to file {CREDENTIALS_FILE}: {e}")
        return

    print(f"File {CREDENTIALS_FILE} encrypted successfully.")


def decrypt_file():
    """Decrypt an encrypted file using the master password from MPASS_FILE."""
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"File {CREDENTIALS_FILE} does not exist.")
        return

    password = load_master_password()

    with open(CREDENTIALS_FILE, 'rb') as file:
        salt = file.readline().strip()
        encrypted_data = file.read()

    key = create_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print(f"Decryption failed: {e}")
        return

    with open(CREDENTIALS_FILE, 'wb') as file:
        file.write(decrypted_data)

    print(f"File {CREDENTIALS_FILE} decrypted successfully.")

# Prompt user to set a master password and store it securely.
def set_master_password():
    while True:
        password = getpass.getpass("Set Master Password: ")
        confirm_password = getpass.getpass("Confirm Master Password: ")

        if password == confirm_password:
            salt = os.urandom(16)
            key = create_key(password, salt)
            fernet = Fernet(key)

            with open(MPASS_FILE, 'wb') as file:
                file.write(salt + b'\n' + base64.urlsafe_b64encode(key))

            print("Master password has been set and stored securely.")
            return
        else:
            print("Passwords do not match. Please try again.")


# Verify the master password
def verify_master_password(password: str) -> bool:
    with open(MPASS_FILE, 'rb') as file:
        salt = file.readline().strip()
        stored_key = file.readline().strip()

    key = create_key(password, salt)
    stored_key = base64.urlsafe_b64decode(stored_key)

    if key == stored_key:
        return True
    else:
        return False


def load_master_password() -> str:
    if not os.path.exists(MPASS_FILE):
        print("Master password file not found. Exiting.")
        exit(1)

    with open(MPASS_FILE, 'rb') as file:
        salt = file.readline().strip()
        stored_key = file.readline().strip()

    password = input("Enter your master password: ")
    key = create_key(password, salt)
    stored_key = base64.urlsafe_b64decode(stored_key)

    if key != stored_key:
        print("Invalid master password.")
        exit(1)

    return password