type_flowers = input()
count_flowers = float(input())
budget = float(input())
cost = 0

if type_flowers == "Roses":
    cost = count_flowers * 5
    if count_flowers>80:
        cost = cost * 0.9
elif type_flowers == "Dahlias":
    cost = count_flowers * 3.8
    if count_flowers >90:
        cost = cost * 0.85
elif type_flowers == "Tulips":
    cost = count_flowers * 2.8
    if count_flowers > 80:
        cost = cost * 0.85
elif type_flowers == "Narcissus":
    cost = count_flowers * 3
    if count_flowers  < 120:
        cost = cost * 1.15
elif type_flowers == "Gladiolus":
    cost = count_flowers * 2.5
    if count_flowers < 80:
        cost = cost * 1.2

if budget < cost:
    money = cost-budget
    print(f'Not enough money, you need {money:.2f} leva more.')
else :
    money = budget-cost
    print(f'Hey, you have a great garden with {count_flowers:.0f} {type_flowers} and {money:.2f} leva left.')


