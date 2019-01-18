num = int(input())
dict_clothes = {}

for i in range(0,num):
    line = input().split(' -> ')
    clothes = line[1].split(',')

    if line[0] in dict_clothes:
        for x in clothes:
            if x in dict_clothes[line[0]]:
                dict_clothes[line[0]][x] +=1
            else:
                dict_clothes[line[0]][x] = 1
    else:
        dict_clothes[line[0]] = {}
        for x in clothes:
            if x in dict_clothes[line[0]]:
                dict_clothes[line[0]][x] +=1
            else:
                dict_clothes[line[0]][x] = 1

search = input()
for x in dict_clothes:
    print(f'{x} clothes:')
    for y in dict_clothes[x]:
        # list = dict_clothes[x]
        # counter = dict_clothes[x].count(y)
        if x + ' ' + y == search:
            print(f'* {y} - {dict_clothes[x][y]} (found!)')
        else:
            print(f'* {y} - {dict_clothes[x][y]}')