import math

record = float(input())
distance = float(input())
speed = float(input())

time_for_dist = distance*speed
slowing = math.floor(distance/50)
slowing = slowing*30
time_for_dist+=slowing

if time_for_dist<record:
    print(f'Yes! The new record is {time_for_dist:.2f} seconds.')
else:
    slow = time_for_dist-record
    print(f'No! He was {slow:.2f} seconds slower.')