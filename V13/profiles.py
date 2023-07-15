import sqlite3
import error  # Importing error.py
import password  # Importing password.py
import search  # Importing search.py


db_exists = False  # Used to check in database exists


def main_menu():
    while True:
        global db_exists
        conn = sqlite3.connect('profile.db')
        cursor = conn.cursor()

        if not db_exists:
            try:
                # Creating the table even if it already exists
                create_table_query = 'CREATE TABLE profile (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, city TEXT, pass_prot BOOLEAN);'
                cursor.execute(create_table_query)
            except:
                pass
            db_exists = True  # Program will not try to create the table again

        conn.commit()  # Commit the changes to the database

        print('1. Login')
        print('2. Options')
        print('3. Exit')

        while True:
            choice_p = input('Enter your choice : ')

            if not choice_p.isdigit():  # Checking if input has alphabets
                print('Error:Invalid Input,Input contained String')
                error.error_handle(100)

            else:
                choice_p = int(choice_p)

            if choice_p not in [1, 2, 3]:  # Checking if the input is out of range
                print('Error:Invalid Input')
                error.error_handle(101)

            elif choice_p == 1:
                prof_data = get_profile_data()

                if prof_data is not None:
                    city = prof_data[2]
                    return city
                else:  # User has failed to enter correct password or username OR has chose to go back to main menu
                    break

            elif choice_p == 2:
                option()
                break

            elif choice_p == 3:  # Closing program
                return True


def get_profile_data():
    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()

    prof_name = input('Enter the profile name : ')

    name_list = []  # Used to append all usernames from database
    prof_list = []
    cursor.execute('SELECT * FROM profile')

    for row in cursor:  # View the table
        name_list.append(row[1])
        prof_list.append(row)

    if prof_name in name_list:
        cursor.execute('SELECT * FROM profile')
        prof_index = name_list.index(prof_name)

        prof_prot_check = password.pass_prot_check(prof_name)

        if prof_prot_check:
            if password.pass_check(prof_name):
                data = prof_list[prof_index]
                print()
                return data

        else:  # If the profile has no password protection
            data = prof_list[prof_index]
            print()
            return data

    else:  # Used to search the entered profile name, if entered profile name is not in database
        data = search.fuzz_search(prof_name, name_list, 'select_prof_city')
        print()

        if data:
            return data

        else:  # If the user as entered a profile name that is not there within the database
            return None


def option():
    while True:
        print()
        print('1. Add new profile')
        print('2. Remove profile')
        print('3. Edit profile')
        print('4. Search profile')
        print('5. Go back to profile selection')

        while True:
            choice_o = input('Enter your choice : ')

            if not choice_o.isdigit():  # Checking if input has alphabets
                print('Error:Invalid Input,Input contained String')
                error.error_handle(100)

            elif int(choice_o) not in [1, 2, 3, 4, 5]:  # Checking if input is out of range
                print('Error:Invalid Input')
                error.error_handle(101)

            else:
                choice_o = int(choice_o)
                break

        print()

        if choice_o == 1:
            add_prof()

        elif choice_o == 2:
            del_prof()

        elif choice_o == 3:
            edit_prof()

        elif choice_o == 4:
            search_prof()

        elif choice_o == 5:
            break


def add_prof():
    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()

    prof_name = input('Enter name of the profile : ')
    prof_city = input('Enter name of the city : ')
    pass_prot = password.pass_create(prof_name)
    q_add_rec = f"INSERT INTO profile (name,city,pass_prot) VALUES ('{prof_name}','{prof_city}',{pass_prot});"
    cursor.execute(q_add_rec)
    conn.commit()
    conn.close()

    print(prof_name, '- Added successfully')
    print()


def del_prof():
    prof_data = get_profile_data()
    if prof_data is not None:
        conn = sqlite3.connect('profile.db')
        cursor = conn.cursor()

        prof_id = prof_data[0]
        prof_name = prof_data[1]

        q_del_rec = f"DELETE FROM profile WHERE id = {prof_id};"
        cursor.execute(q_del_rec)
        conn.commit()
        conn.close()

        print(prof_name,'- removed successfully!')

    else:
        print('Profile was not removed')

    print()


def edit_prof():
    prof_data = get_profile_data()

    if not prof_data:
        print('Profile was not selected for editing')
        return False

    else:
        conn = sqlite3.connect('profile.db')
        cursor = conn.cursor()

        prof_id = prof_data[0]

        print('1. Edit name')
        print('2. Edit city')

        choice = input('Enter your choice : ')

        if not choice.isdigit():  # Checking if input has no alphabets
            print('Error:Invalid Input,Input contained String')
            error.error_handle(100)

        else:
            choice = int(choice)

        if choice in [1,2]:
            if choice == 1:
                prof_new_name = input('Enter new profile : ')
                edit_prof_cmd = f"UPDATE profile SET name = '{prof_new_name}' WHERE id = '{prof_id}';"

            else:
                prof_new_city = input('Enter new profile : ')
                edit_prof_cmd = f"UPDATE profile SET name = '{prof_new_city}' WHERE id = '{prof_id}';"

            cursor.execute(edit_prof_cmd)
            conn.commit()
            conn.close()

        else:
            print('Error:Invalid Input')


def search_prof():
    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()
    name_list = []

    for row in cursor:  # View the table
        name_list.append(row[1])

    while True:
        print('1. Accurate search')
        print('2. Non-Accurate search')
        print('3. Go back')

        while True:
            choice = input('Enter your choice : ')

            if not choice.isdigit():  # Checking if input has alphabets
                print('Error:Invalid Input,Input contained String')
                error.error_handle(100)

            elif int(choice) not in [1, 2, 3]:  # Checking if input is out of range
                print('Error:Invalid Input')
                error.error_handle(101)

            else:
                choice = int(choice)
                break

        if choice == 3:
            break

        print()

        prof_name = input('Enter the name of the profile: ')

        while True:
            if prof_name == 'BACK':
                break
            search.fuzz_search_prof(prof_name, name_list, choice)
            prof_name = input('Enter the name of the another profile or enter BACK to go back : ')
