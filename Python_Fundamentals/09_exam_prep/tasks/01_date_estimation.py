from datetime import date

input_year, input_month, input_date = input().split('-')

curr_year = 2018
curr_month = 8
curr_date = 26

d0 = date(int(input_year), int(input_month), int(input_date))
d1 = date(curr_year, curr_month, curr_date)

d = d0 - d1

if d.days > 0:
    print(f'{d.days + 1} days left')
elif d.days == 0:
    print('Today date')
else:
    print('Passed')
