import sqlite3
import error  # Importing error.py


db_exists = False  # Used to check in database exists


def profile():
    while True:
        global db_exists
        conn = sqlite3.connect('profile.db')
        cursor = conn.cursor()

        if not db_exists:
            try:
                # Creating the table even if it already exists
                create_table_query = """CREATE TABLE profile (id INTEGER PRIMARY KEY, name TEXT, city TEXT);"""
                cursor.execute(create_table_query)
            except:
                pass
            db_exists = True  # Program will not try to create the table again

        conn.commit() # Commit the changes to the database

        row_list = []  # Used to append all rows
        count_t = 0
        cursor.execute('SELECT * FROM profile')
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
            city = row_list[int(choice_p) - 1][2]
            print()
            return city


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

        if choice_o == 1:
            add_prof()

        elif choice_o == 2:
            del_prof()

        else:
            break


def add_prof():
    print()

    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()

    counter = 0
    cursor.execute('SELECT * FROM profile')
    for _ in cursor:
        counter += 1

    prof_name = input('Enter name of the profile : ')
    prof_city = input('Enter name of the city : ')
    q_add_rec = f"INSERT INTO profile (id,name,city) VALUES ({counter + 1},'{prof_name}','{prof_city}');"
    cursor.execute(q_add_rec)
    conn.commit()
    conn.close()

    print()


def del_prof():
    print()
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

    choice_p = input('Enter your choice : ')

    if not choice_p.isdigit():  # Checking if input has no alphabets
        print('Error:Invalid Input,Input contained String')
        error.error_handle(100)
        
    else:
        choice_p = int(choice_p)

    in_row = count_l.index(choice_p)
    q_row = row_l[in_row]

    q_get_rec = f'SELECT * FROM profile WHERE id IS {q_row}'
    cursor.execute(q_get_rec)
    
    for row in cursor:
        del_usr = row[1]

    q_del_rec = f"DELETE FROM profile WHERE id = {q_row};"

    cursor.execute(q_del_rec)
    conn.commit()
    conn.close()
    print(del_usr, '- removed successfully!')
    print()
