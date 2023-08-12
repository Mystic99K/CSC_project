import sqlite3
import os
import sys

if os.name == "nt":
    import msvcrt
else:
    import getch

from utils import *

def login(cursor, crypt_cipher, selected_prof):
    while True:
        # Get profile name and if exist in the database
        in_prof_name = input('Enter the profile name: ')

        try:
            cursor.execute(f"""SELECT * FROM profile WHERE name = '{in_prof_name}';""")
        except sqlite3.Error as err:
            print(f"""Error: SQL command execution failed "{err}".""")


        matched_prof = parse_prof(cursor.description, cursor.fetchone())
        
        if matched_prof is None:
            print('Error: No such profile found, re-enter the name.')
            error_handle(103)
            continue
                
        in_prof_password = input_password("Enter the profile's password: ")
        dnc_password_hash = crypt_cipher.decrypt(matched_prof["password_hash"]).decode()
        if in_prof_password == dnc_password_hash:
            input(f"""Success: You are logged in as '{matched_prof["name"]}' (ENTER): """)
            for char in matched_prof.keys():
                selected_prof[char] = matched_prof[char]
            break
        else:
            input("""Error: Password entered is wrong (ENTER): """)
            continue
        
def parse_prof(cursor_table_desc, record):
    if record is None:
        return None

    prof = {}
    for i in range(0, len(cursor_table_desc)):
        field_name = cursor_table_desc[i][0]
        field_data = record[i]

        prof[field_name] = field_data
    return prof


def input_password(prompt='Password: '):
    print(prompt, end='', flush=True)
    password = ''
    
    while True:
        char = ""
        if os.name == "nt":
            char = msvcrt.getch().decode('utf-8')
        else:
            char = getch.getch()
            
        if char == '\r' or char == '\n':
            break
        
        if char == '\x08':
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    
    print()
    return password


    # sys.stdout.write(prompt)
    # sys.stdout.flush()
    
    # password = ''
    # while True:
    #     char = getch.getch()
    #     if char == '\r' or char == '\n':
    #         break
    #     if char == '\x7f':
    #         password = password[:-1]
    #         sys.stdout.write('\b \b')
    #         sys.stdout.flush()
    #     else:
    #         password += char
    #         sys.stdout.write('*')
    #         sys.stdout.flush()
    # sys.stdout.write('\n')
    # sys.stdout.flush()
    # return password
