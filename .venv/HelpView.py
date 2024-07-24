#  HelpView.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

# ANSI escape codes for colors
reset = "\033[0m"
bold = "\033[1m"
green = "\033[92m"


def help_view():
    print(f"{bold}==========={reset} {green}{bold}HELP{reset} {bold}==========={reset}")
