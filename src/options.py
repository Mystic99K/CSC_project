import sqlite3
import getpass
from utils import *
from login import parse_prof
from ui import *
from rich.table import Table
from rich.console import Console
from rich import box

def options(conn, cursor, crypt_cipher, selected_prof):
    while True:
        cls()

        option_menu = "\n=========================OPTIONS=========================\n"
        option_menu += "1. Create new profile\n"
        option_menu += "2. Delete your profile\n"
        option_menu += "3. Edit your profile\n"
        option_menu += "4. Search your profile (not yet)\n"
        option_menu += "5. Display all saved profiles (not yet)\n"
        option_menu += "6. Exit options menu\n"

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
                print(f"""Success: Profile '{prof["name"]}' has been successfully added.""")
            input("Enter to go back: ")
        elif choice_o == "2":
            if not selected_prof:
                input("You haven't yet logged in (ENTER): ")
                continue
            
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
                    print('Logging out and switching to Guest...')
                    selected_prof.clear()
                input("Enter to go back: ")
            else:
                pass
        elif choice_o == "3":
            if not selected_prof:
                input("You haven't yet logged in (ENTER): ")
                continue
            
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
            
        elif choice_o == "5":
            try:
                cursor.execute(f"""SELECT * FROM profile""")
            except sqlite3.Error as err:
                print(f"""Error: SQL command execution failed "{err}".""")

            console = Console()
            table = Table(show_header=True, header_style="bold magenta", show_lines=True, box=box.DOUBLE_EDGE)
            table.add_column("Name", style="green")
            table.add_column("City", style="cyan")

            rows = cursor.fetchall()
            for row in rows:
                table.add_row(f"{row[1]}", f"{row[2]}")

            console.print(table)

            input("Enter to go back: ")

        elif choice_o == "6":
            break
        else:
            input("Error: Invalid input (ENTER): ")
