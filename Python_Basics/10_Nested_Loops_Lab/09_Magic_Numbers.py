n = int(input())

for i in range(1, 9):
    for j in range(1, 9):
        for k in range(1, 9):
            for l in range(1, 9):
                for m in range(1, 9):
                    for p in range(1, 9):
                        magic = i * j * k * l * m * p
                        if magic == n:
                            print(str(i) + str(j) + str(k) + str(l) + str(m) + str(p) + ' ', end="")
