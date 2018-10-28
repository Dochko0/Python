import math

first_brother = float(input())
second_brother = float(input())
third_brother = float(input())
father = float(input())

all_time = 1/((1/first_brother)+(1/second_brother) + (1/third_brother))
all_time = all_time*1.15

print('Cleaning time: ' + format(all_time, '.2f'))

time_left = father - all_time

if time_left>=0:
    print('Yes, there is a surprise - time left -> ' + str(math.floor(time_left)) + ' hours.')
else:
    print('No, there isn\'t a surprise - shortage of time -> ' + str(math.ceil((time_left*-1))) + ' hours.')