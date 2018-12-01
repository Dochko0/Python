max_sum = 0
win_name = ''
while True:
    name = input()
    sum = 0
    if name == 'STOP':
        break
    for n in name:
        sum += ord(n)

    if sum >= max_sum:
        max_sum = sum
        win_name = name

print(f'Winner is {win_name} - {max_sum}!')
