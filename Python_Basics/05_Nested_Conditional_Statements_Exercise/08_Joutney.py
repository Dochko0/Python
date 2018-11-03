budget = float(input())
season = input()
cost = 0

if budget<=100:
    if season == 'summer':
        cost = budget*0.3
        print('Somewhere in Bulgaria')
        print(f'Camp - {cost:.2f}')
    elif season == 'winter':
        cost = budget*0.7
        print('Somewhere in Bulgaria')
        print(f'Hotel - {cost:.2f}')
elif 100<budget<=1000:
    if season == 'summer':
        cost = budget*0.4
        print('Somewhere in Balkans')
        print(f'Camp - {cost:.2f}')
    elif season == 'winter':
        cost = budget*0.8
        print('Somewhere in Balkans')
        print(f'Hotel - {cost:.2f}')
elif 1000<budget:
        cost = budget*0.9
        print('Somewhere in Europe')
        print(f'Hotel - {cost:.2f}')
