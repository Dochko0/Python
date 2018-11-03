budget = float(input())
category = input()
count_of_people = int(input())

if 1<=count_of_people<=4:
    budget = budget*0.25
elif 5<=count_of_people<=9:
    budget = budget*0.4
elif 10<=count_of_people<=24:
    budget = budget*0.5
elif 25<=count_of_people<=49:
    budget = budget*0.6
elif 50<=count_of_people:
    budget = budget*0.75

billets_price = 0.0

if category== 'Normal':
    billets_price =  249.99*count_of_people
elif category == 'VIP':
    billets_price = 499.99*count_of_people

if budget<billets_price:
     print(f'Not enough money! You need {billets_price-budget:.2f} leva.')
else:
     print(f'Yes! You have {budget-billets_price:.2f} leva left.')