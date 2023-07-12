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

            if choice_p == 1:
                city = select_profile_city()

                if city:
                    return city
                else:  # User has failed to enter correct password or username OR has chose to go back to main menu
                    break

            elif choice_p == 2:
                option()
                break

            elif choice_p == 3:  # Closing program
                return True


def select_profile_city():
    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()

    prof = input('Enter the profile name : ')

    row_name = []  # Used to append all usernames from database
    cursor.execute('SELECT * FROM profile')

    for row in cursor:  # View the table
        row_name.append(row[1])

    if prof in row_name:
        row_list = []
        cursor.execute('SELECT * FROM profile')
        prof_index = row_name.index(prof)  # Getting index of the user's data, used for splicing

        for row in cursor:  # Getting all data from database, this will be then spliced
            row_list.append(row)

        prof_prot_check = password.pass_prot_check(prof)  # Used to check if the profile is password protected or not

        if prof_prot_check:
            if password.pass_check(prof):  # Used to check if the user knows the password of the profile
                city = row_list[prof_index][2]
                print()
                return city

        else:  # If the profile has no password protection
            city = row_list[prof_index][2]
            return city

    else:  # Used to search the entered profile name, if entered profile name is not in database
        city = search.fuzz_search(prof, row_name, 'select_prof_city')
        print()

        if city:
            return city

        else:  # If the user as entered a profile name that is not there within the database
            return False


def option():
    print()
    while True:
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
    while True:
        conn = sqlite3.connect('profile.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM profile')
        counter = 0
        count_l = []
        row_l = []

        for row in cursor:  # Displaying all profiles
            counter += 1
            print(counter, '. ', row[1], sep='')
            count_l.append(counter)
            row_l.append(row[0])

        while True:
            choice_p = input('Enter your choice : ')

            if not choice_p.isdigit():  # Checking if input has no alphabets
                print('Error:Invalid Input,Input contained String')
                error.error_handle(100)

            else:
                choice_p = int(choice_p)
                break

        in_row = count_l.index(choice_p)
        q_row = row_l[in_row]
        q_get_rec = f'SELECT * FROM profile WHERE id IS {q_row}'
        cursor.execute(q_get_rec)

        for row in cursor:
            del_usr = row[1]

        pass_prot_ch = password.pass_prot_check(del_usr)

        if pass_prot_ch:
            prof_del = password.pass_check(del_usr)

            if not prof_del:
                break

        else:
            prof_del = True

        q_del_rec = f"DELETE FROM profile WHERE id = {q_row};"
        cursor.execute(q_del_rec)
        conn.commit()
        conn.close()
        break

    if prof_del:
        print(del_usr, '- removed successfully!')

    else:
        print(del_usr, '- was not removed')

    print()


def edit_prof():
    prof_name = select_profile_name()

    if not prof_name:
        print('Profile was not selected for editing')
        return False

    else:
        prof_id = select_profile_id(prof_name)

        print('1. Edit name')
        print('2. Edit city')

        choice = input('Enter your choice : ')

        if not choice.isdigit():  # Checking if input has no alphabets
            print('Error:Invalid Input,Input contained String')
            error.error_handle(100)

        else:
            choice = int(choice)

        if choice == 1:
            prof_new_name = input('Enter new profile : ')

            conn = sqlite3.connect('profile.db')
            cursor = conn.cursor()
            edit_prof_cmd = f"UPDATE profile SET name = '{prof_new_name}' WHERE id = '{prof_id}';"
            cursor.execute(edit_prof_cmd)
            conn.commit()
            conn.close()

        elif choice == 2:  # fix this
            prof_new_city = input('Enter new profile : ')

            conn = sqlite3.connect('profile.db')
            cursor = conn.cursor()
            edit_prof_cmd = f"UPDATE profile SET name = '{prof_new_city}' WHERE id = '{prof_id}';"
            cursor.execute(edit_prof_cmd)
            conn.commit()
            conn.close()

        else:
            print('Error')


def select_profile_name():
    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()

    prof_name = input('Enter the profile name : ')

    row_name = []  # Used to append all rows
    cursor.execute('SELECT * FROM profile')

    for row in cursor:  # View the table
        row_name.append(row[1])

    if prof_name in row_name:
        row_list = []
        cursor.execute('SELECT * FROM profile')
        prof_index = row_name.index(prof_name)

        for row in cursor:  # View the table
            row_list.append(row)

        prof_prot_check = password.pass_prot_check(prof_name)  # ______CHANGE VARIABLES NAME______

        if prof_prot_check:
            if password.pass_check(prof_name):
                name = row_list[prof_index][1]
                print()
                return name

        else:
            name = row_list[prof_index][1]
            return name

    else:
        name = search.fuzz_search(prof_name, row_name,
                                  'select_profile_name')  # __________Error for inputting wrong profile name__________
        print()

        if name:
            return name

        else:
            return False


def select_profile_id(prof_name):
    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()
    row_name = []  # Used to append all rows
    cursor.execute('SELECT * FROM profile')

    for row in cursor:  # View the table
        row_name.append(row[1])

    row_list = []
    cursor.execute('SELECT * FROM profile')
    prof_index = row_name.index(prof_name)

    for row in cursor:  # View the table
        row_list.append(row)

    prof_id = row_list[prof_index][0]
    prof_prot_check = password.pass_prot_check(prof_name)  # ______CHANGE VARIABLES NAME______

    if prof_prot_check:
        if password.pass_check(prof_name):
            print()
            return prof_id

    else:
        return prof_id


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


main_menu()
