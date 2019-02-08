import math

def calculate_dist(first_point, second_point):
    point_x = abs(first_point.x - second_point.x)
    point_y = abs(first_point.y - second_point.y)
    distance = math.sqrt(point_x**2+point_y**2)
    return distance

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))

first_point = Point(point1[0], point1[1])
second_point = Point(point2[0], point2[1])

result = calculate_dist(first_point,second_point)
print(f'{result:.3f}')

