import sqlite3
import password
import search
from clscreen import cls


def get_profile_data(prof_name=None):
    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()

    cls()
    name_list = []  # Used to append all usernames from database
    prof_list = []
    cursor.execute('SELECT * FROM profile')

    for row in cursor:  # View the table
        name_list.append(row[1])
        prof_list.append(row)

    if prof_name is None:
        prof_name = input('Enter the profile name : ')

        if prof_name in name_list:
            prof_index = name_list.index(prof_name)
            prof_data = prof_list[prof_index]
            pass_prot_check = prof_data[3]

            if pass_prot_check == 3:
                if password.pass_check(prof_name):
                    print()
                    return prof_data

            else:  # If the profile has no password protection
                print()
                return prof_data

        else:  # Used to search the entered profile name, if entered profile name is not in database
            data = search.fuzz_search(prof_name, name_list)
            print()

            if data:
                return data

            else:  # If the user as entered a profile name that is not there within the database
                return None

    else:
        prof_index = name_list.index(prof_name)
        prof_data = prof_list[prof_index]
        return prof_data
