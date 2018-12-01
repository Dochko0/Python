while True:
    country = input()
    if country == 'End':
        break
    target = int(input())
    while True:
        money = input()
        if money.isdigit():
            target -= int(money)
        elif not money.isdigit():
            break
        if target <= 0:
            print(f'Going to {country}!')
            break
