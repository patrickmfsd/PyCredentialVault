#  AddCredential.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

import getpass
import os

# ANSI escape codes for colors
reset = "\033[0m"
bold = "\033[1m"
green = "\033[92m"

# File to store credentials
CREDENTIALS_FILE = 'credentials.txt'


def add_credential():
    print(f"{bold}==========={reset} {green}{bold}ADD NEW CREDENTIAL{reset} {bold}==========={reset}")
    username = prompt_non_empty_input("Username: ")
    if username is None:
        return

    password = getpass.getpass("Password: ").strip()
    if not password:
        print("Error: Password cannot be empty.")
        return

    url = prompt_non_empty_input("URL: ")
    if url is None:
        return

    # Write the credential to a file
    if save_credential(username, password, url):
        print("Credential Added Successfully.\n")


def prompt_non_empty_input(prompt):
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
