def pass_check():

    pass_f = open('password.txt', 'r')
    list1= pass_f.readline()

    print(list1.split())

pass_check()