import math

def distantion(first, second):
    point_x = abs(first.x - second.x)
    point_y = abs(first.y - second.y)
    distance = math.sqrt(point_x ** 2 + point_y ** 2)
    return distance

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


lines = int(input())
all_points = []
for i in range(0,lines):
    point_x, point_y = map(int,input().split())
    all_points.append(Point(point_x,point_y))

calculations = {}

for j in range(0,lines):
    first_point = all_points[j]
    for x in range(j+1,lines):
        second_point = all_points[x]
        dist = distantion(first_point, second_point)
        if dist not in calculations:
            calculations[dist] = []
            calculations[dist].append(f'({all_points[j].x}, {all_points[j].y})')
            calculations[dist].append(f'({all_points[x].x}, {all_points[x].y})')

calculations_sort_dict = sorted(calculations.items())

print(f'{calculations_sort_dict[0][0]:.3f}')
print(calculations_sort_dict[0][1][0])
print(calculations_sort_dict[0][1][1])


