import getpass
import os

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"

# File to store credentials
CREDENTIALS_FILE = 'credentials.txt'

def viewCredentials():
    print(f"{BOLD}==========={RESET} {GREEN}{BOLD}VIEW CREDENTIALS{RESET} {BOLD}==========={RESET}")

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
            print(f"{BOLD} Credential {index}{RESET}")
            print(f" Username: {username}")
            print(f" Password: {password}")
            print(f" URL: {url}\n")
            print(f"----------------------------------------")

