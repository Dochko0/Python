name = input()
count = 1
grade = 0.0
while count <= 12:
    curr = float(input())
    if curr >= 4:
        grade = grade + curr
        count += 1

average = grade / 12
if average >= 4:
    print(f'{name} graduated. Average grade: {average:.2f}')
