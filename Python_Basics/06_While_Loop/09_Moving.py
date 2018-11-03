width_free_space = float(input())
length_free_space = float(input())
height_free_space = float(input())
value = width_free_space * length_free_space * height_free_space
cartons = 0

while cartons <= value:
    line = input()
    if line == "Done":
        break
    else:
        line = int(line)

    cartons += line

if cartons > value:
    diff = cartons - value
    print(f'No more free space! You need {diff:.0f} Cubic meters more.')
else:
    diff = value - cartons
    print(f'{diff:.0f} Cubic meters left.')
