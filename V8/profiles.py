import sqlite3
import error  # Importing error.py
import password  # Importing password.py

db_exists = False  # Used to check in database exists


def profile():
    while True:
        global db_exists
        conn = sqlite3.connect('profile.db')
        cursor = conn.cursor()

        if not db_exists:
            try:
                # Creating the table even if it already exists
                create_table_query = """CREATE TABLE profile (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, city TEXT, pass_prot BOOLEAN);"""
                cursor.execute(create_table_query)
            except:
                pass
            db_exists = True  # Program will not try to create the table again

        conn.commit()  # Commit the changes to the database

        row_list = []  # Used to append all rows
        count_t = 0
        cursor.execute('SELECT * FROM profile')
        print()
        for row in cursor:  # View the table
            count_t += 1
            print(count_t, '. ', row[1], sep='')
            row_list.append(row)

        print(count_t + 1, '. Options', sep='')
        print(count_t + 2, '. Exit', sep='')

        conn.close()  # Close the connection to the database

        choice_p = input('Enter your choice : ')

        if not choice_p.isdigit():  # Checking if input has no alphabets
            print('Error:Invalid Input,Input contained String')
            error.error_handle(100)

        elif int(choice_p) == count_t + 1:
            option()

        elif int(choice_p) == count_t + 2:  # Stopping program
            return True

        elif int(choice_p) > count_t + 2:
            print('Error:Invalid Input')
            error.error_handle(101)

        else:
            choice_p = int(choice_p)
            prof_name = row_list[choice_p - 1][1]
            prof_prot_check = password.pass_prot_check(prof_name)  # ______CHANGE VARIABLES NAME______
            if prof_prot_check:
                if password.pass_check(prof_name):
                    city = row_list[choice_p - 1][2]
                    print()
                    return city

                else:
                    continue


def option():
    print()
    while True:
        print('1. Add new profile')
        print('2. Remove profile')
        print('3. Go back to profile selection')

        while True:
            choice_o = input('Enter your choice : ')

            if not choice_o.isdigit():  # Checking if input has no alphabets
                print('Error:Invalid Input,Input contained String')
                error.error_handle(100)

            elif choice_o != '1' and choice_o != '2' and choice_o != '3':  # Checking if input is not out of range
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

        else:
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
    prof_del = False
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
