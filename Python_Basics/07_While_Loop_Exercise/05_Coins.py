import math

price = float(input())
coins = 0

while price > 0:
    if price / 2 >= 1:
        coins += math.floor(price / 2)
        price = round(price % 2, 2)
    elif price / 1 >= 1:
        coins += math.floor(price / 1)
        price = round(price % 1, 2)
    elif price / 0.5 >= 1:
        coins += math.floor(price / 0.5)
        price = round(price % 0.5, 2)
    elif price / 0.2 >= 1:
        coins += math.floor(price / 0.2)
        price = round(price % 0.2, 2)
    elif price / 0.1 >= 1:
        coins += math.floor(price / 0.1)
        price = round(price % 0.1, 2)
    elif price / 0.05 >= 1:
        coins += math.floor(price / 0.05)
        price = round(price % 0.05, 2)
    elif price / 0.02 >= 1:
        coins += math.floor(price / 0.02)
        price = round(price % 0.02, 2)
    elif price / 0.01 >= 1:
        coins += math.floor(price / 0.01)
        price = round(price % 0.01, 2)

print(coins)
