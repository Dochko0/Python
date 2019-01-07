side1 = float(input())
side2 = float(input())


def calculate_area(a, h):
    area = (a * h) / 2
    return area


def printable(a, h):
    print(f'{calculate_area(a,h):.12g}')
    # check_area = calculate_area(a, h)
    # check_10 = check_area * 10
    # if check_10 % 10 == 0:
    #     print(f'{check_area:.0f}')
    # else:
    #     print(f'{check_area}')


printable(side1, side2)
