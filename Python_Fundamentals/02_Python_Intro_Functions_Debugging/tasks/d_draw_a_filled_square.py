num = int(input())


def draw_border(num):
    print('-' * (2 * num))


def draw_body(num):
    for i in range(0, int(num -2)):
        print('-' + '\/' * (num-1) +'-')


draw_border(num)
draw_body(num)
draw_border(num)
