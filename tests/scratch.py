def input_password(prompt='Password: '):
    print(prompt, end='', flush=True)
    password = ''
    
    while True:
        char = ""
        if os.name == "nt":
            char = msvcrt.getch().decode('utf-8')
        else:
            char = getch.getch()
            
        if char == '\r' or char == '\n':
            break
        
        
        
        if char == '\b':
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    
    print()
    return password