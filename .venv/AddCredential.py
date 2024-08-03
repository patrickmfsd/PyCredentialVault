import getpass
import os
from EncryptionHelper import encrypt_file

# ANSI escape codes for colors
reset = "\033[0m"
bold = "\033[1m"
green = "\033[92m"

# File to store credentials
CREDENTIALS_FILE = 'credentials.txt'


def add_credential():
    print(f"\n{green}{bold}=========== ADD NEW CREDENTIAL ==========={reset}\n")
    print("Password is obscured when typing.\n")
    username = prompt_for_non_empty_input("Username: ")
    if username is None:
        return

    password = getpass.getpass("Password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return

    url = prompt_for_non_empty_input("URL: ")
    if url is None:
        return

    # Write the credential to a file
    if save_credential(username, password, url):
        encrypt_file(CREDENTIALS_FILE)
        print("Credential Added Successfully.\n")


def prompt_for_non_empty_input(prompt):
    value = input(prompt).strip()
    if not value:
        print("Error: This field cannot be empty.")
        return None
    return value


def save_credential(username, password, url):
    try:
        with open(CREDENTIALS_FILE, 'a') as file:
            file.write(f"{username},{password},{url}\n")
        return True
    except IOError as e:
        print(f"Error: Could not write to file. {e}")
        return False
