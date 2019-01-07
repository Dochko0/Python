name = input()
age = int(input())
town = input()
salary = float(input())

print(f'Name: {name}')
print(f'Age: {age}')
print(f'Town: {town}')
print(f'Salary: ${salary:.2f}')

if age<18:
    print(f'Age range: teen')
elif age<70:
    print(f'Age range: adult')
else:
    print(f'Age range: elder')

if salary<500:
    print(f'Salary range: low')
elif salary<2000:
    print(f'Salary range: medium')
else:
    print(f'Salary range: high')


