import sqlite3
import getpass

from utils import *
import utils # for changing state of utils.loggedin

def login(cursor, crypt_cipher, selected_prof):
    while True:
        # Get profile id and if exist in the database
        in_prof_id = input('Enter the profile id: ')


        try:
            cursor.execute(
                """SELECT * FROM profile WHERE id = ?;""",
                (in_prof_id)
            )
        except sqlite3.Error as err:
            print(f"""Error: SQL command execution failed "{err}".""")


        matched_prof = parse_prof(cursor.description, cursor.fetchone())
        if matched_prof is None:
            print('Error: No such profile found, re-enter the id.')
            error_handle(103)
            continue
                
        in_prof_password = getpass.getpass("Enter the profile's password: ")
        dnc_password_hash = crypt_cipher.decrypt(matched_prof["password_hash"]).decode()
        if in_prof_password == dnc_password_hash:
            input(f"""Success: You are logged in as '{matched_prof["name"]}' (ENTER): """)
            utils.loggedin = True
            for key in matched_prof.keys():
                selected_prof[key] = matched_prof[key]
            break
        else:
            input("""Error: Password entered is wrong, re-enter password (ENTER): """)
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
