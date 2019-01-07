def first(a):
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            printirane(j)
        print()


def second(a):
    for i in range(a, 1, -1):
        for j in range(1, i):
            printirane(j)
        print()


def printirane(j):
    print(f'{j} ', end=" ")


def pyramid(a):
    first(a)
    second(a)


a = int(input())
pyramid(a)
