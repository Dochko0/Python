def enter():
    return int(input())


def check_number(num):
    if num < 0:
        return 'negative'
    elif num > 0:
        return 'positive'
    else:
        return 'zero'


def result_print():
    num = enter()
    print(f'The number {num} is {check_number(num)}.')


result_print()
