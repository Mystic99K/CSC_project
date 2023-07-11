from fuzzywuzzy import fuzz


def fuzz_search(name,name_list):
    check = False
    for i in name_list:
        if best_match > 75:
            check = True

    if check:
        print('Did you mean :',end=' ')




names = ["shashank", "tariq", "rainer", "ananth"]

user_input = input("Enter a name: ")

for i in names:

    best_match = fuzz.ratio(user_input, i)

    if best_match > 75:
        print("Did you mean:", i)
        print(best_match)
