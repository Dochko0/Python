username_passwords = {}
counter = 0
while True:
    line = input().split(' -> ')
    if line[0] == 'login':
        break
    # if username_passwords[line[0]] in username_passwords:
    #     username_passwords[line[0]] = line[1]
    # else:
    username_passwords[line[0]] = line[1]

while True:
    login = input().split(' -> ')
    if login[0] == 'end':
        break
    if login[0] in username_passwords and username_passwords[login[0]] == login[1]:
        print(f'{login[0]}: logged in successfully')
    else:
        print(f'{login[0]}: login failed')
        counter+=1

print(f'unsuccessful login attempts: {counter}')
