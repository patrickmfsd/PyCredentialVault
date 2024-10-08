# main.py
# Created by Patrick Mifsud on 24/7/24.
# Copyright © 2024 Patrick Mifsud. All rights reserved.

from ViewCredentials import view_credentials
from AddCredential import add_credential
from HelpView import help_view
from EncryptionHelper import *

import os
import getpass
import sys

MPASS_FILE = 'masterpw.text'
CREDENTIALS_FILE = 'credentials.txt'

stored_password = None


def initialize_credentials_file():
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'wb') as file:
            pass  # Create an empty file


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac


# Exit handling, encrypt file > clear terminal > exit program
def handle_quit():
    print("Quitting...")
    encrypt_file(CREDENTIALS_FILE)
    clear_terminal()
    sys.exit()


def main():
    initialize_credentials_file()

    # ANSI escape codes for colors
    reset = "\033[0m"
    bold = "\033[1m"
    teal = "\033[96m"
    green = "\033[92m"
    red = "\033[91m"

    # App Header
    print(f"\n{bold}=========== PASSWORD MANAGER ==========={reset}\n")
    print(" By Patrick Mifsud                 v0.1 ")
    print("\n----------------------------------------")

    initialize_master_pass()

    # Action List
    actions = {
        'N': add_credential,
        'V': view_credentials,
        '?': help_view,
        'Q': handle_quit
    }

    # Main Menu Display
    while True:
        print("\n----------------------------------------")
        print(f" {green}{bold}(N){reset} New Credential")
        print(f" {green}{bold}(V){reset} View Credentials")
        print("----------------------------------------")
        print(f" {teal}{bold}(?){reset} Help           | {red}{bold}(Q){reset} Quit")
        print("----------------------------------------\n")
        choice = input(f"{bold}Enter Option:{reset} ").upper()

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid Choice. Please enter a valid option.\n")


if __name__ == "__main__":
    main()