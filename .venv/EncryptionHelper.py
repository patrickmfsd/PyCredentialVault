import base64
import os
import getpass
import sys
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

MPASS_FILE = 'masterpw.txt'
CREDENTIALS_FILE = 'credentials.txt'
stored_password = None

def create_key(password: str, salt: bytes) -> bytes:
    """Create a key from the password and salt using PBKDF2HMAC."""
    password_bytes = password.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key

def encrypt_file(filename: str):
    """Encrypt the contents of a text file in place."""
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    password = load_master_password()

    salt = os.urandom(16)
    key = create_key(password, salt)
    fernet = Fernet(key)

    try:
        with open(filename, 'rb') as file:
            data = file.read()
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return

    encrypted_data = fernet.encrypt(data)

    try:
        with open(filename, 'wb') as file:
            file.write(salt + b'\n' + encrypted_data)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
        return

    print(f"File {filename} encrypted successfully.")

def decrypt_file(filename: str):
    """Decrypt the contents of a text file in place."""
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    password = load_master_password()

    try:
        with open(filename, 'rb') as file:
            lines = file.readlines()
            if len(lines) < 2:
                print("File does not have the expected format.")
                return
            salt = lines[0].strip()
            encrypted_data = lines[1]
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return

    key = create_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print(f"Decryption failed: {e}")
        return

    try:
        with open(filename, 'wb') as file:
            file.write(decrypted_data)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
        return

    print(f"File {filename} decrypted successfully.")

def set_master_password():
    """Prompt user to set and store a master password."""
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

def verify_master_password(password: str) -> bool:
    """Verify the provided master password."""
    if not os.path.exists(MPASS_FILE):
        return False

    with open(MPASS_FILE, 'rb') as file:
        lines = file.readlines()
        if len(lines) != 2:
            print("Master password file is incorrectly formatted.")
            return False

        salt = lines[0].strip()
        stored_key = lines[1].strip()

    key = create_key(password, salt)
    stored_key = base64.urlsafe_b64decode(stored_key)

    return key == stored_key

def load_master_password() -> str:
    """Load and return the master password if it is already stored."""
    global stored_password

    if stored_password is not None:
        return stored_password

    if not os.path.exists(MPASS_FILE) or os.path.getsize(MPASS_FILE) == 0:
        print("Master password file not found or is empty. Exiting.")
        sys.exit(1)

    with open(MPASS_FILE, 'rb') as file:
        lines = file.readlines()
        if len(lines) != 2:
            print("Master password file is incorrectly formatted.")
            sys.exit(1)

        salt = lines[0].strip()
        stored_key = lines[1].strip()

    password = getpass.getpass("Enter your master password: ")
    key = create_key(password, salt)
    stored_key = base64.urlsafe_b64decode(stored_key)

    if key != stored_key:
        print("Invalid master password.")
        sys.exit(1)

    stored_password = password
    return password


def initialize_master_pass():
    """Initialize or verify the master password."""
    global stored_password

    if os.path.exists(MPASS_FILE) and os.path.getsize(MPASS_FILE) > 0:
        # Check if the stored master password is valid
        password = getpass.getpass("\nEnter your master password: ")
        if verify_master_password(password):
            stored_password = password
        else:
            print("Invalid Master Password. Exiting application.\n")
            sys.exit(1)
    else:
        print("Master password file does not exist or is empty.")
        set_master_password()
        stored_password = getpass.getpass("\nEnter your master password: ")