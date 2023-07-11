import pickle
import sqlite3
import error  # Importing error.py


def pass_create(name):
    while True:
        prof_pass_v = input('Do you want the profile to be password protected? (Y/y/N/n) : ')
        if prof_pass_v != 'Y' and prof_pass_v != 'y' and prof_pass_v != 'N' and prof_pass_v != 'n':
            print('Error:Invalid Input')
            error.error_handle(100)
        else:
            if prof_pass_v in ['Y', 'y']:
                while True:
                    while True:
                        prof_pass_1 = input('Enter the password for the new profile (8 Characters Min) : ')
                        if len(prof_pass_1) < 8:
                            print('Error:Entered password is not at lest 8 characters long')
                        else:
                            break
                    prof_pass_2 = input('Enter the password again : ')
                    if prof_pass_1 == prof_pass_2:
                        break

                    else:
                        print('Error:Entered password do not match')
                        error.error_handle(102)
                pass_prot = 1
                break

            else:
                pass_prot = 0
                return pass_prot
    
    pass_code = prof_pass_1
    pass_f = open('password.dat', 'wb')
    pass_l = [name, pass_code]
    pickle.dump(pass_l, pass_f)
    pass_f.close()
    return pass_prot


def pass_check(name):
    while True:
        check = False
        pass_code = input("Enter profile's password or CANCEL to cancel : ")
        if pass_code == 'CANCEL':
            return check
        pass_f = open('password.dat', 'rb')
        try:
            while True:
                pass_l = pickle.load(pass_f)
                if pass_l[0] == name and pass_l[1] == pass_code:
                    check = True
                    return check
        except EOFError:
            pass
        pass_f.close()
        if not check:
            print('Error:Incorrect password entered')
            error.error_handle(103)


def pass_prot_check(name):
    conn = sqlite3.connect('profile.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM profile')
    pass_prot_ch = False
    for row in cursor:  # Going through all profiles
        if row[1] == name and row[3] == 1:
            pass_prot_ch = True

    return pass_prot_ch
