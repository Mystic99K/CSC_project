import os

def cls():
    if os.name == 'nt': # for windows
        os.system('cls')
    else:
        os.system('clear') # for unix based shells, like Linux or macOS

if __name__ == '__main__' :
    import time
    print('this is test.')
    if input("y/n : ") == 'y':
        cls()
    else:
        pass