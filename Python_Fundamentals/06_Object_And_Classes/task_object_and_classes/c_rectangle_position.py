def is_inside(first_rectangle, second_rectangle):
    if first_rectangle.top <= second_rectangle.top and first_rectangle.bottom >= second_rectangle.bottom and \
            first_rectangle.left >= second_rectangle.left and \
            first_rectangle.right <= second_rectangle.right:
        print("Inside")
    else:
        print('Not inside')


class Rectangle:
    def __init__(self, left, bottom, width, height):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
        self.right = left + width
        self.top = bottom + height


rectengles_list = []

for i in range(0, 2):
    read_input = list(map(int, input().split()))
    rectengles_list.append(Rectangle(read_input[0], read_input[1], read_input[2], read_input[3]))

check_is_inside = is_inside(rectengles_list[0], rectengles_list[1])
