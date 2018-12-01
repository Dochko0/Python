import math

width = float(input())
length = float(input())
height = float(input())
astronaut = float(input())

ship = width*length*height
room_value = (astronaut+0.4)*2*2
people = math.floor(ship/room_value)

if people<3:
    print('The spacecraft is too small.')
elif people>10:
    print('The spacecraft is too big.')
else:
    print(f'The spacecraft holds {people} astronauts.')