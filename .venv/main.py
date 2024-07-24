#  main.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

from ViewCredentials import view_credentials
from AddCredential import add_credential
from HelpView import help_view
from Settings import settings


def main():
    # Action List
    actions = {
        'N': add_credential,
        'V': view_credentials,
        'H': help_view,
        'S': settings,
        'Q': exit
    }

    # ANSI escape codes for colors
    reset = "\033[0m"
    bold = "\033[1m"
    teal = "\033[96m"
    green = "\033[92m"
    red = "\033[91m"

    # Main Menu Display
    while True:
        print(f"{bold}==========={reset} {green}{bold}PASSWORD MANAGER{reset} {bold}==========={reset}")
        print(" By Patrick Mifsud                 v0.1 ")
        print("----------------------------------------")
        print(f" {green}{bold}(N){reset} New Credential")
        print(f" {green}{bold}(V){reset} View Credentials")
        print("----------------------------------------")
        print(f" {bold}(S){reset} Settings  |  {teal}{bold}(H){reset} Help  |  {red}{bold}(Q){reset} Quit ")
        print("----------------------------------------")
        choice = input(f"{bold}Enter Option:{reset} ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid Choice. Please enter valid option.\n")


if __name__ == "__main__":
    main()
