num = int(input())


def check_negative(num):
    if num < 0:
        num = num * -1
    sum_even_odd(num)


def sum_even_odd(val):
    even = 0
    odd = 0
    val = str(val)
    for v in val:
        v = int(v)
        if v % 2 == 0:
            even += v
        else:
            odd += v
    multiply(even, odd)


def multiply(even, odd):
    print(even * odd)


check_negative(num)
