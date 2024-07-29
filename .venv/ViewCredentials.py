#  ViewCredentials.py
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


def view_credentials():
    print(f"{bold}==========={reset} {green}{bold}VIEW CREDENTIALS{reset} {bold}==========={reset}")

    if not os.path.exists(CREDENTIALS_FILE):
        print("Credential File Exists.\n")
        return

    with open(CREDENTIALS_FILE, 'r') as file:
        lines = file.readlines()
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
