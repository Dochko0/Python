project_parts = int(input())
money_by_point = float(input())
points = 0
isEven = False
while True:
    if project_parts <= 0:
        break

    cicle = int(input())

    if isEven:
        cicle = cicle * 2
        isEven = False
    else:
        isEven = True

    points += cicle
    project_parts-=1

prize = points*money_by_point

print(f'The project prize was {prize:.2f} lv.')
