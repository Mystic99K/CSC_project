import os


# START: Utility Functions
def cls():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:
        os.system('clear')  # Unix based shells
    # pass