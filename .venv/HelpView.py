#  HelpView.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"

def help():
    print(f"{BOLD}==========={RESET} {GREEN}{BOLD}HELP{RESET} {BOLD}==========={RESET}")
