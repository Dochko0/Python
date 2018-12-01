import math

sushi_type = input()
restaurant = input()
portions = int(input())
order = input()
price = 0

if restaurant != 'Sushi Zone' \
        and restaurant != 'Sushi Time' \
        and restaurant != 'Sushi Bar' \
        and restaurant != 'Asian Pub':
    print(f'{restaurant} is invalid restaurant!')
else:
    if restaurant == 'Sushi Zone':
        if sushi_type == 'sashimi':
            price = portions * 4.99
        elif sushi_type == 'maki':
            price = portions * 5.29
        elif sushi_type == 'uramaki':
            price = portions * 5.99
        elif sushi_type == 'temaki':
            price = portions * 4.29
    elif restaurant == 'Sushi Time':
        if sushi_type == 'sashimi':
            price = portions * 5.49
        elif sushi_type == 'maki':
            price = portions * 4.69
        elif sushi_type == 'uramaki':
            price = portions * 4.49
        elif sushi_type == 'temaki':
            price = portions * 5.19
    elif restaurant == 'Sushi Bar':
        if sushi_type == 'sashimi':
            price = portions * 5.25
        elif sushi_type == 'maki':
            price = portions * 5.55
        elif sushi_type == 'uramaki':
            price = portions * 6.25
        elif sushi_type == 'temaki':
            price = portions * 4.75
    elif restaurant == 'Asian Pub':
        if sushi_type == 'sashimi':
            price = portions * 4.5
        elif sushi_type == 'maki':
            price = portions * 4.8
        elif sushi_type == 'uramaki':
            price = portions * 5.5
        elif sushi_type == 'temaki':
            price = portions * 5.5

    if order == 'Y':
        price = math.ceil(price*1.2)
        print(f'Total price: {price} lv.')
    else:
        print(f'Total price: {math.ceil(price)} lv.')