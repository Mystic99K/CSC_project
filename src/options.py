import sqlite3

from utils import *
# from login import parse_prof
# from login import input_password
from ui import *

from rich.table import Table
from rich.console import Console
from rich import box
import json


def write_conf(setting_obj):
    with open('config.json','w') as conf_file:
        conf = json.dumps(setting_obj)
        conf_file.write(conf)
        
def read_conf():
    with open('config.json','r') as conf_file:
        conf = json.loads(conf_file.read())
        return conf

def options(conn, cursor, crypt_cipher, selected_prof):
    while True:
        cls()
        print_menu(
            main_console,
            'Main Menu',
            'bright_cyan',
            'bright_yellow',
            Text()
                .append("1. Change unit\n")
                .append("2. Change alignment\n")
                .append("6. Exit options menu")
        )

        choice_o = input("Enter your choice: ")

        if choice_o == "1":
            unit_conf = unit_menu()
            conf = read_conf()
            conf['unit'] == unit_conf
        elif choice_o == "2":
            print('') #trq do this partttt me hab to goooooooooooooooooooooo
            conf = read_conf()
            conf['unit'] == unit_conf
        elif choice_o == "3":
            break
        else:
            input("Error: Invalid input (ENTER): ")
