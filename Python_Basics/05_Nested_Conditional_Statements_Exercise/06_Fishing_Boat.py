budget = float(input())
season = input()
fishmens = float(input())

cost = 0

if season == "Spring":
    if fishmens <= 6:
        cost = 3000 * 0.90
    elif 6 < fishmens <= 11:
        cost = 3000 * 0.85
    elif fishmens > 11:
        cost = 3000 * 0.75
elif season == "Summer" or season == "Autumn":
    if fishmens <= 6:
        cost = 4200 * 0.90
    elif 6 < fishmens <= 11:
        cost = 4200 * 0.85
    elif fishmens > 11:
        cost = 4200 * 0.75
elif season == "Winter":
    if fishmens <= 6:
        cost = 2600 * 0.90
    elif 6 < fishmens <= 11:
        cost = 2600 * 0.85
    elif fishmens > 11:
        cost = 2600 * 0.75

if fishmens % 2 == 0 and season != "Autumn":
    cost = cost * 0.95

if budget < cost:
    diff = cost - budget
    print(f'Not enough money! You need {diff:.2f} leva.')
else:
    diff = budget - cost
    print(f'Yes! You have {diff:.2f} leva left.')
