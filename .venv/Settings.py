#  Settings.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

# ANSI escape codes for colors
reset = "\033[0m"
bold = "\033[1m"
green = "\033[92m"
red = "\033[91m"

def settings():
    print(f"\n{bold}=============== SETTINGS ==============={reset}")
    print("------------------------------------")
    print(f" {green}{bold}(MP){reset} Change Master Password")
    print("------------------------------------")
    print(f"{red}------------------------------------{reset}")
    print(f" {red}{bold}(R){reset} {red}RESET PASSWORD DATABASE{reset}")
    print(f"{red}------------------------------------{reset}")
    print(f"\n{bold}========================================{reset}\n")

    choice = input(f"{bold}Enter Option:{reset} ")
