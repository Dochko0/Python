import math

hour = int(input())
min = int(input())

min = min + 15

if min >= 60:
    plus_hour = math.floor(min / 60)
    min = min%60
    hour += plus_hour

if hour > 24:
    hour = math.floor(hour / 24)
elif hour==24:
    hour=0

if min < 10:
    print(str(hour) + ':0' + str(min))
else:
    print(str(hour) + ':' + str(min))
