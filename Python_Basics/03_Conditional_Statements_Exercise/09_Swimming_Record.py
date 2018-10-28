import math

world_record = float(input())
distance = float(input())
time_per_meter = float(input())

time_for_swimming = distance * time_per_meter
slowing = math.floor((distance / 15)) * 12.5
total_time = slowing + time_for_swimming

if total_time>=world_record:
    extra_seconds = total_time-world_record
    print(f'No, he failed! He was {extra_seconds:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')