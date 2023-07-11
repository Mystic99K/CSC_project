from fuzzywuzzy import fuzz
import error  # Importing error.py


def fuzz_search(prof_name, name_list):
    check = False
    best_match_l = []

    for name_1 in name_list:
        best_match = fuzz.ratio(prof_name, name_1)

        if best_match > 60:
            check = True
            best_match_l.append(name_1)

    if len(best_match_l) == 0:
        print('Error:No such profile found, going back to main menu')
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
        print('Error:No such profile found, going back to main menu')
        error.error_handle(104)
        return False

