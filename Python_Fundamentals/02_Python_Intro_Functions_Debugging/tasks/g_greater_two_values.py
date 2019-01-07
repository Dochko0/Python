value_type = input()
val1 = input()
val2 = input()


def compare_values(a, b):
    if a > b:
        printable(a)
    else:
        printable(b)


def printable(greater_value):
    print(greater_value)


compare_values(val1, val2)
