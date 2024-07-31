#  ViewCredentials.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

import getpass
import os

from EncryptionHelper import *


# ANSI escape codes for colors
reset = "\033[0m"
bold = "\033[1m"
green = "\033[92m"

# File to store credentials
CREDENTIALS_FILE = 'credentials.txt'


def inspect_file_contents():
    """Inspect the file contents after decryption."""
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'rb') as file:
            contents = file.read()
            print("File Contents After Decryption:", contents)
            try:
                decoded_contents = contents.decode('utf-8')
                print("Decoded Contents:", decoded_contents)
            except UnicodeDecodeError:
                print("Failed to decode file contents.")
    else:
        print(f"File {CREDENTIALS_FILE} does not exist.")


def view_credentials():
    print(f"\n{green}{bold}=========== VIEW CREDENTIALS ==========={reset}")

    if not os.path.exists(CREDENTIALS_FILE):
        print("Credential File Does Not Exist.\n")
        return

    try:
        decrypt_file(CREDENTIALS_FILE)
        inspect_file_contents()

        with open(CREDENTIALS_FILE, 'rb') as file:
            decrypted_data = file.read()

        # Decode the decrypted data
        decoded_data = decrypted_data.decode('utf-8')
        lines = decoded_data.splitlines()

        if not lines:
            print("No Credentials Stored.\n")
            return

        for index, line in enumerate(lines, start=1):
            username, password, url = line.strip().split(',')
            print(f"{bold}Credential {index}{reset}")
            print(f"    Username: {username}")
            print(f"    Password: {password}")
            print(f"    URL: {url}\n")
            print(f"----------------------------------------\n")

    except Exception as e:
        print(f"Error: {e}")

    print(f"\n{green}{bold}========================================{reset}\n")