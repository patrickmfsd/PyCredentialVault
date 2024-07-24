#  main.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

from ViewCredentials import viewCredentials
from AddCredential import addCredential
from HelpView import help
from Settings import settings


def main():
    # Action List
    actions = {
        'N': addCredential,
        'V': viewCredentials,
        'H': help,
        'S': settings,
        'Q': exit
    }

    # ANSI escape codes for colors
    RESET = "\033[0m"
    BOLD = "\033[1m"
    TEAL = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"

    # Main Menu Display
    while True:
        print(f"{BOLD}==========={RESET} {GREEN}{BOLD}PASSWORD MANAGER{RESET} {BOLD}==========={RESET}")
        print(" By Patrick Mifsud                 v0.1 ")
        print("----------------------------------------")
        print(f" {GREEN}{BOLD}(N){RESET} New Credential")
        print(f" {GREEN}{BOLD}(V){RESET} View Credentials")
        print("----------------------------------------")
        print(f" {BOLD}(S){RESET} Settings  |  {TEAL}{BOLD}(H){RESET} Help  |  {RED}{BOLD}(Q){RESET} Quit ")
        print("----------------------------------------")
        choice = input(f"{BOLD}Enter Option:{RESET} ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid Choice. Please enter valid option.\n")


if __name__ == "__main__":
    main()
