import cryptography.fernet as crypt
import sqlite3
from ui import *
from utils import *
from login import login
from show_weather import show_weather
from options import options

def __main__():
    db_exists = False
    
    conn = sqlite3.connect('../db/profile.db')
    cursor = conn.cursor()

    crypt_cipher = crypt.Fernet(PASSWRD_ENCRYPTION_KEY)
    selected_prof = {}
    
    if not db_exists:
        try:
            # Creating the table even if it already exists
            create_table_query = 'CREATE TABLE "profile" ("id" INTEGER UNIQUE, "name" TEXT UNIQUE, "city" TEXT, "password_hash" BLOB, PRIMARY KEY("id" AUTOINCREMENT));'
            cursor.execute(create_table_query)
        except:
            pass
        db_exists = True  # Program will not try to create the table again
        
        conn.commit()  # Commit the changes to the database

    while True:
        mconsole.clear()

        menu = "\n=========================MAIN MENU=========================\n"
        if selected_prof:
            menu += f"""[Currently logged in as '{selected_prof["name"]}']\n"""
        else:
            menu += f"""[Currently logged in as Guest]\n"""
        menu += "1. Login\n"
        menu += "2. Show weather\n"
        menu += "3. Options\n"
        if selected_prof:
            menu += "4. Logout\n"
            menu += "5. Exit program\n"
        else:
            menu += "4. Exit program\n"
        print(menu)
        usr_choice = input('Enter your choice: ')


        if usr_choice == "1":
            login(cursor, crypt_cipher, selected_prof)
        elif usr_choice == "2":
            show_weather(selected_prof)
        elif usr_choice == "3":
            options(conn, cursor, crypt_cipher, selected_prof)
        elif selected_prof:
            if usr_choice == "4":
                selected_prof = {}
                mconsole.clear()
                print("Logged out! Switching to Guest...")
                input("Enter to go back:")    
            elif usr_choice == "5":
                print("Exited program!")
                break
        elif usr_choice == "4":
            print("Exited program!")
            break
        else:
            input("Error: Invalid input (ENTER): ")
            continue
    
    conn.close()

__main__()