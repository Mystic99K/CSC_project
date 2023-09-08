import cryptography.fernet as crypt
import sqlite3
from ui import *
from utils import *
from login import login
from show_weather import show_weather
from options import options

console = Console()


def __main__():
    db_exists = False
    
    conn = sqlite3.connect('../db/profile.db')
    cursor = conn.cursor()

    crypt_cipher = crypt.Fernet(PASSWRD_ENCRYPTION_KEY)
    selected_prof = {}
    
    guestMenu = Text()\
        .append("1. Login\n") \
        .append("2. Show weather\n") \
        .append("3. Options\n") \
        .append("4. Exit program")
                
    if not db_exists:
        try:
            # Creating the table even if it already exists
            create_table_query = 'CREATE TABLE "profile" ("id" INTEGER UNIQUE, "name" TEXT UNIQUE, "city" TEXT, "password_hash" BLOB, "setting" TEXT ,PRIMARY KEY("id" AUTOINCREMENT));'
            cursor.execute(create_table_query)
        except:
            pass
        db_exists = True  # Program will not try to create the table again
        
        conn.commit()  # Commit the changes to the database

    while True:
        cls()
        
        print(f"Logged in as - Guest")
        print_menu( main_console, 'Main Menu', 'bright_cyan', 'bright_yellow', guestMenu )

        usr_choice = input('Enter your choice: ')

        if usr_choice == "1":
            login(cursor, crypt_cipher, selected_prof)
            print(selected_prof)
            input()
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
