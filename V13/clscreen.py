import os


def cls():
    if os.name == 'nt': # for windows
        os.system('cls')
    else:
        os.system('clear') # for unix based shells, like Linux or macOS
