class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def get_width(self):
        return abs(self.upper_right.x - self.upper_left.x)

    def get_heigh(self):
        return  abs(self.upper_left.y - self.bottom_left.y)

    def perimeter(self):
        return self.get_heigh()*2 + self.get_width()*2

    def area(self):
        return  self.get_width()*self.get_heigh()

    def __str__(self):
        return f'Box: {self.get_width()}, {self.get_heigh()}\nPerimeter: {self.perimeter()}\nArea: {self.area()}'

boxes = []

while True:
    line = input()
    if line == 'end':
        break

    points = line.split(' | ')
    u_l = Point(points[0].split(':')[0], points[0].split(':')[1])
    u_r = Point(points[1].split(':')[0], points[1].split(':')[1])
    b_l = Point(points[2].split(':')[0], points[2].split(':')[1])
    b_r = Point(points[3].split(':')[0], points[3].split(':')[1])

    boxes.append(Box(u_l,u_r,b_l,b_r))


for box in boxes:
    print(box)