name = input()
count = 1
grade = 0.0
count_of_poor = 0

while count <= 12:
    curr = float(input())
    if curr >= 4:
        grade = grade + curr
        count += 1
        count_of_poor = 0
    else:
        count_of_poor += 1

    if count_of_poor >= 2:
        break

if count < 12:
    print(f'{name} has been excluded at {count} grade')
else:
    average = grade / 12
    print(f'{name} graduated. Average grade: {average:.2f}')
