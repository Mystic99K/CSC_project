import cryptography.fernet as crypt
import sqlite3

from utils import *
from login import login
from show_weather import show_weather
from options import options
from richcolor import *

def __main__():
    db_exists = False
    conn = sqlite3.connect('../db/profile.db')
    cursor = conn.cursor()

    crypt_cipher = crypt.Fernet(PASSWRD_ENCRYPTION_KEY)
    selected_prof = None

    while True:
        cls()

        if not db_exists:
            try:
                # Creating the table even if it already exists
                create_table_query = 'CREATE TABLE profile (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, city TEXT, pass_prot BOOLEAN);'
                cursor.execute(create_table_query)
            except:
                pass
            db_exists = True  # Program will not try to create the table again

        conn.commit()  # Commit the changes to the database

        fpanel = Text(justify="center")
        fpanel.append("Main Menu", style="bold blue")
        fpanel.append(" - ")
        print(selected_prof['name'])
        if selected_prof:
            fpanel.append(f"Logged in as ", style="italic red")
            print(Panel(fpanel))
        else:
            fpanel.append("Logged in as Guest", style="italic red")
            print(Panel(fpanel))

        print("1. Login")
        print("2. Show weather")
        print("3. Options")
        print("4. Exit program")

        usr_choice = input('Enter your choice: ')


        if usr_choice == "1":
            login(conn, cursor, crypt_cipher, selected_prof)
        elif usr_choice == "2":
            show_weather(selected_prof)
        elif usr_choice == "3":
            options(conn, cursor, crypt_cipher, selected_prof)
        elif usr_choice == "4":
            print("Exited program!")
            break
        else:
            input("Error: Invalid input (ENTER): ")
            continue
    
    conn.close()

__main__()