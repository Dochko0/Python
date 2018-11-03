import math

hour_exam = int(input())
minute_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

all_minute_exam = hour_exam * 60 + minute_exam
all_minute_arrive = hour_arrive * 60 + minute_arrive

if all_minute_arrive <= all_minute_exam:
    if all_minute_exam - all_minute_arrive <= 30:
        diff = all_minute_exam - all_minute_arrive
        print("On time")
        if diff != 0:
            print(f'{diff} minutes before the start')
    else:
        diff = all_minute_exam - all_minute_arrive
        diff_hour = math.floor(diff / 60)
        diff_min = math.floor(diff % 60)
        if diff_hour == 0:
            print("Early")
            print(f'{diff} minutes before the start')
        elif 0 <= diff_min < 10:
            print("Early")
            print(f'{diff_hour}:0{diff_min} hours before the start')
        else:
            print("Early")
            print(f'{diff_hour}:{diff_min} hours before the start')
else:
    diff = all_minute_arrive - all_minute_exam
    diff_hour = math.floor(diff / 60)
    diff_min = math.floor(diff % 60)
    if diff_hour == 0:
        print("Late")
        print(f'{diff} minutes after the start')
    else:
        if 0<=diff_min<10:
            print("Late")
            print(f'{diff_hour}:0{diff_min} hours after the start')
        else:
            print("Late")
            print(f'{diff_hour}:{diff_min} hours after the start')
