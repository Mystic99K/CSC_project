import sqlite3
import getpass
import error  # Importing error.py
import encrypt  # Importing encrypt.py


def pass_create(name):
    while True:
        prof_pass_v = input('Do you want the profile to be password protected? (Y/y/N/n) : ')
        if prof_pass_v not in ['Y', 'y', 'N', 'n']:
            print('Error:Invalid Input')
            error.error_handle(100)
        else:
            if prof_pass_v in ['Y', 'y']:
                while True:
                    while True:
                        prof_pass_1 = getpass.getpass('Enter the password for the new profile (8 Characters Min) : ')
                        if len(prof_pass_1) < 8:
                            print('Error:Entered password is not at lest 8 characters long')
                        else:
                            break
                    prof_pass_2 = getpass.getpass('Enter the password again : ')
                    if prof_pass_1 == prof_pass_2:
                        break

                    else:
                        print('Error:Entered password do not match')
                        error.error_handle(102)
                pass_prot = 1
                break

            else:
                return None

    prof_pass = prof_pass_1
    enc_prof_pass = encrypt.encrypt_pass(prof_pass)

    return enc_prof_pass


def pass_check(name):
    while True:
        check = False
        pass_code = getpass.getpass("Enter profile's password or CANCEL to cancel : ")
        if pass_code == 'CANCEL':
            return check

        dec_pass = encrypt.decrypt_pass(name)

        if dec_pass == pass_code:
            check = True
            return check

        else:
            print('Error:Incorrect password entered')
            error.error_handle(103)

