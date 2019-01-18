dict_position = {}
dict_salary = {}
dict_age = {}


while True:
    line = input().split(" -> ")

    if line[0] == 'filter base':
        break

    if line[1].isdigit():
        dict_age[line[0]] = line[1]
    else:
        try:
            line[1] = float(line[1])
            dict_salary[line[0]] = line[1]
        except:
            dict_position[line[0]] = line[1]

command = input()
if command == 'Position':
    for x in dict_position:
        print(f'Name: {x}')
        print(f'Position: {dict_position[x]}')
        print('====================')
elif command == 'Salary':
    for x in dict_salary:
        print(f'Name: {x}')
        print(f'Salary: {dict_salary[x]}')
        print('====================')
else:
    for x in dict_age:
        print(f'Name: {x}')
        print(f'Age: {dict_age[x]}')
        print('====================')


