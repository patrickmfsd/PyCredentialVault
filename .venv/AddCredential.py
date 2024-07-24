import getpass
import os

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"

# File to store credentials
CREDENTIALS_FILE = 'credentials.txt'

def addCredential():
    print(f"{BOLD}==========={RESET} {GREEN}{BOLD}ADD NEW CREDENTIAL{RESET} {BOLD}==========={RESET}")
    username = promptNonEmptyInput("Username: ")
    if username is None:
        return

    password = getpass.getpass("Password: ").strip()
    if not password:
        print("Error: Password cannot be empty.")
        return

    url = promptNonEmptyInput("URL: ")
    if url is None:
        return

    # Write the credential to a file
    if save_credential(username, password, url):
        print("Credential Added Successfully.\n")

def promptNonEmptyInput(prompt):
    value = input(prompt).strip()
    if not value:
        print("Error: This field cannot be empty.")
        return None
    return value


def saveCredential(username, password, url):
    try:
        with open(CREDENTIALS_FILE, 'a') as file:
            file.write(f"{username},{password},{url}\n")
        return True
    except IOError as e:
        print(f"Error: Could not write to file. {e}")
        return False
