n = int(input())
curr = 1
isBigger = False
for rows in range(1, n + 1):
    for cols in range(1, rows + 1):
        if curr > n:
            isBigger = True
            break
        print(str(curr) + " ", end="")
        curr += 1
    if isBigger:
        break
    print()
