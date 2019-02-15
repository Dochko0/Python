from datetime import date

input_date = list(map(int, input().split('-')))
d1 = date(2018, 8, 26)
d2 = date(input_date[0], input_date[1], input_date[2])

delta = d2-d1

if delta.days>0:
    print(f'{delta.days+1} days left')
elif delta.days<0:
    print('Passed')
else:
    print('Today date')

