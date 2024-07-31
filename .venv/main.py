#  main.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

from ViewCredentials import view_credentials
from AddCredential import add_credential
from HelpView import help_view
from Settings import settings
from EncryptionHelper import *

import os

MPASS_FILE = 'masterpw.text'

CREDENTIALS_FILE = 'credentials.txt'

stored_password = None

def initialize_credentials_file():
    """Create an empty credentials file if it does not exist."""
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'wb') as file:
            pass  # Create an empty file

def handle_quit():
    print("Quitting...")
    encrypt_file(CREDENTIALS_FILE)
    exit()

def main():
    global stored_password

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

    # Check if MPASS_FILE is empty or does not exist
    if not os.path.exists(MPASS_FILE) or os.path.getsize(MPASS_FILE) == 0:
        print("Please set a Master Password to securely\nstore your credentials.\n")
        set_master_password()

    # Prompt user for the master password and verify it
    password = getpass.getpass("\nEnter your master password: ")
    if not verify_master_password(password):
        print("Invalid Master Password. Exiting application.\n")
        return

    # Action List
    actions = {
        'N': add_credential,
        'V': view_credentials,
        'H': help_view,
        'S': settings,
        'Q': handle_quit
    }


    # Main Menu Display
    while True:
        print("\n----------------------------------------")
        print(f" {green}{bold}(N){reset} New Credential")
        print(f" {green}{bold}(V){reset} View Credentials")
        print("----------------------------------------")
        print(f" {bold}(S){reset} Settings  |  {teal}{bold}(H){reset} Help  |  {red}{bold}(Q){reset} Quit ")
        print("----------------------------------------\n")
        choice = input(f"{bold}Enter Option:{reset} ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid Choice. Please enter valid option.\n")


if __name__ == "__main__":
    main()
