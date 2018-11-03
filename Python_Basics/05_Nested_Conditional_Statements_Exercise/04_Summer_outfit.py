temperature = int(input())
time = input().lower()

if 10<=temperature<=18:
    if time == "morning":
        print(f'It\'s {temperature} degrees, get your Sweatshirt and Sneakers.')
    elif time == 'afternoon':
        print(f'It\'s {temperature} degrees, get your Shirt and Moccasins.')
    elif time == 'evening':
        print(f'It\'s {temperature} degrees, get your Shirt and Moccasins.')
elif 18<temperature<24:
    if time == "morning":
        print(f'It\'s {temperature} degrees, get your Shirt and Moccasins.')
    elif time == 'afternoon':
        print(f'It\'s {temperature} degrees, get your T-Shirt and Sandals.')
    elif time == 'evening':
        print(f'It\'s {temperature} degrees, get your Shirt and Moccasins.')
elif 25<=temperature:
    if time == "morning":
        print(f'It\'s {temperature} degrees, get your T-Shirt and Sandals.')
    elif time == 'afternoon':
        print(f'It\'s {temperature} degrees, get your Swim Suit and Barefoot.')
    elif time == 'evening':
        print(f'It\'s {temperature} degrees, get your Shirt and Moccasins.')