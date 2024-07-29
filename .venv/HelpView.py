#  HelpView.py
#  Created by Patrick Mifsud on 24/7/24.
#  Copyright © 2024 Patrick Mifsud. All rights reserved.

# ANSI escape codes for colors
reset = "\033[0m"
bold = "\033[1m"
teal = "\033[96m"


def help_view():
    # Display the help content
    print(f"\n{teal}{bold}================= HELP ================={reset}\n")
    print("To navigate the app, use your keyboard.\n"
          "To choose an option, type the\n"
          "corresponding option.")

    print(f"\n{bold}----------{reset} {bold}Adding Credentials{reset} {bold}----------{reset}")
    print("To add a new credential, from the main\n"
          "menu, choose the (N) option. Follow the\n"
          "prompts and enter the username, password,\n"
          "and URL.")

    print(f"\n{bold}-----------{reset} {bold}View Credentials{reset} {bold}-----------{reset}")
    print("To add a view saved credential, from the\n"
          "main menu, choose the (V) option.")

    print(f"\n{bold}--------------{reset} {bold}View Help{reset} {bold}----------------{reset}")
    print("To view this help file, from the main\n"
          "menu, choose the (H) option.")

    print(f"\n{bold}---------------{reset} {bold}Settings{reset} {bold}---------------{reset}")
    print("To view settings, from the main menu,\n"
          "choose the (H) option.\n"
          "From settings you can clear the\n"
          "password database, set/change\n"
          "master password.")
    print(f"\n{teal}{bold}========================================{reset}\n")