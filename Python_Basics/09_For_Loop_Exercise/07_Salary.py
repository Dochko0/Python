num_sites = int(input())
salary = int(input())

for i in range(1, num_sites + 1):
    site = input()

    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print(f'You have lost your salary.')
else:
    print(salary)
