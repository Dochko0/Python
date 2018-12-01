base_camp = 5364
goal = 8848
days = 5

while True:
    if days<=0 or base_camp>=goal:
        break

    night = input()

    if night=='Yes':
        days-=1
        if days<=0:
            break
    elif night == 'END':
        break

    progress = int(input())
    base_camp+=progress


if base_camp<goal:
    print('Failed!')
    print(f'{base_camp}')
else:
    print(f'Goal reached for {6-days} days!')



