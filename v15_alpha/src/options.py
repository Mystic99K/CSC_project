import sqlite3
import getpass

from utils import *

def options(conn, cursor, crypt_cipher, selected_prof):
    while True:
        cls()

        option_menu = "\n=========================OPTIONS=========================\n"
        option_menu += "1. Create new profile\n"
        option_menu += "2. Delete your profile\n"
        option_menu += "3. Edit your profile\n"
        option_menu += "4. Exit options menu\n"

        print(option_menu)
        choice_o = input("Enter your choice: ")

        if choice_o == "1":
            prof = {
                "name": input('Enter name of the profile: '),
                "city": input('Enter name of the city: '),
                "password_hash": crypt_cipher.encrypt(
                    getpass.getpass("Enter profile's password: ").encode("utf-8")
                )
            }

            try:
                cursor.execute(
                    """INSERT INTO profile(name, city, password_hash) VALUES (?, ?, ?);""",
                    (prof["name"], prof["city"], prof["password_hash"])
                )

                conn.commit()
            except sqlite3.Error as err:
                print(f"""Error: SQL command execution failed "{err}".""")
            else:
                print(f"""Success: Profile '{prof["name"]}' has been successfully added. Your profile id is '{cursor.lastrowid}'.""")
            input("Enter to go back: ")
        elif choice_o == "2":
            if input("Warning: You are about to delete your account. Press type 'y' to continue or press enter to stop: "):
                try:
                    cursor.execute(
                        """DELETE FROM profile WHERE id = ?;""",
                        (selected_prof["id"], )
                    )
                    conn.commit()
                except sqlite3.Error as err:
                    print(f"""Error: SQL command execution failed "{err}".""")
                else:
                    print(f"""Success: Profile '{selected_prof["name"]}' has been successfully removed.""")
                input("Enter to go back: ")
            else:
                pass
        elif choice_o == "3":
            in_prof_name = input(f"""Enter new profile name ({selected_prof["name"]}): """)
            if in_prof_name is None:
                in_prof_name = selected_prof["name"]

            in_prof_city = input(f"""Enter new profile city ({selected_prof["city"]}): """)
            if in_prof_city is None:
                in_prof_city = selected_prof["city"]

            try:
                cursor.execute(
                    "UPDATE profile SET name = ?, city = ? WHERE id = ?;",
                    (in_prof_name, in_prof_city, selected_prof["id"])
                )
                conn.commit()
            except sqlite3.Error as err:
                print(f"""Error: SQL command execution failed "{err}".""")
            else:
                print(f"""Success: Profile '{selected_prof["name"]}' has been successfully updated.""")
            input("Enter to go back: ")
        elif choice_o == "4":
            break
        else:
            input("Error: Invalid input (ENTER): ")
