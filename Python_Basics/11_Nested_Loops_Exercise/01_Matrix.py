a = int(input())
b = int(input())
c = int(input())
d = int(input())

for firstRowFirstNum in range(a, b + 1):
    for firstRowSecondNum in range(a, b + 1):
        for secondRowFirstNum in range(c, d + 1):
            for secondRowSecondNum in range(c, d + 1):
                if (firstRowFirstNum + secondRowSecondNum) == (firstRowSecondNum + secondRowFirstNum) \
                        and (firstRowFirstNum != firstRowSecondNum) \
                        and (secondRowFirstNum != secondRowSecondNum):
                    print(f'{firstRowFirstNum}{firstRowSecondNum}')
                    print(f'{secondRowFirstNum}{secondRowSecondNum}')
                    print()
