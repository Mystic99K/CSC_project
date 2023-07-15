from fuzzywuzzy import fuzz
import error  # Importing error.py


def fuzz_search(prof_name, name_list, location):
    check = False
    best_match_l = []

    for name_1 in name_list:
        best_match = fuzz.ratio(prof_name, name_1)

        if best_match > 60:
            check = True
            best_match_l.append(name_1)

    if len(best_match_l) == 0:
        if location == 'select_prof_city':
            print('Error:No such profile found, going back to main menu')
        else:
            print('Error:No such profile found, going back to options menu')
        error.error_handle(104)
        return False

    if check:
        print('Did you mean :', end=' ')
    for name_2 in best_match_l:
        print(name_2, end=' ')

    prof = input('Enter profile name again : ')
    if prof in best_match_l:
        return prof
    else:
        if location == 'select_prof_city':
            print('Error:No such profile found, going back to main menu')
        else:
            print('Error:No such profile found, going back to options menu')
        error.error_handle(104)
        return False


def prof_fuzz_search(name, name_list, search_type):
    while True:
        if search_type == 1:
            check = False
            best_match_l = []

            for name_1 in name_list:
                best_match = fuzz.ratio(name, name_1)

                if best_match > 80:
                    check = True
                    best_match_l.append(name_1)

            if not check:
                print('No such profile found')
                break

            num_prof_found = len(best_match_l)

            if num_prof_found == 1:
                print('Found 1 profile with similar name :', end=' ')
            else:
                print(f'Found {num_prof_found} profiles with similar name :', end=' ')

            for name_2 in best_match_l:
                print(name_2, end=' ')
        else:
            check = False
            best_match_l = []

            for name_1 in name_list:
                best_match = fuzz.ratio(name, name_1)

                if best_match > 50:
                    check = True
                    best_match_l.append(name_1)

            if not check:
                print('No such profile found')
                break

            num_prof_found = len(best_match_l)

            if num_prof_found == 1:
                print('Found 1 profile with similar name :', end=' ')
            else:
                print(f'Found {num_prof_found} profiles with similar name :', end=' ')

            for name_2 in best_match_l:
                print(name_2, end=' ')
