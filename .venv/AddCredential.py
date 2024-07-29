# AddCredential.py
# Created by Patrick Mifsud on 24/7/24.
# Copyright © 2024 Patrick Mifsud. All rights reserved.

import getpass
import os
import validators

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

    url = prompt_and_validate_url()

    # Write the credential to a file
    if save_credential(username, password, url):
        print("Credential Added Successfully.\n")


def prompt_non_empty_input(prompt):
    value = input(prompt).strip()
    if not value:
        print("Error: This field cannot be empty.")
        return None
    return value


def prompt_and_validate_url() -> str:
    """Prompt for a URL and validate it. Keep prompting until a valid URL is provided."""
    while True:
        url = prompt_non_empty_input("URL: ")
        if not url:
            continue  # Prompt again if URL is empty
        if is_valid_url(url):
            return url
        print("Invalid URL. Please enter a valid URL.")


def is_valid_url(url: str) -> bool:
    """Validate a URL using the validators library."""
    return validators.url(url)


def save_credential(username, password, url):
    try:
        with open(CREDENTIALS_FILE, 'a') as file:
            file.write(f"{username},{password},{url}\n")
        return True
    except IOError as e:
        print(f"Error: Could not write to file. {e}")
        return False