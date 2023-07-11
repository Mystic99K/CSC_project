from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import Levenshtein

names = ["shashank", "tariq", "rainer", "ananth"]

user_input = input("Enter a name: ")

for i in names:
    
    best_match = fuzz.ratio(user_input, i)

    if best_match > 80:
        print("Did you mean:", i)
        print(best_match)
    



