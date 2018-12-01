n = int(input())

for row in range (0, n):
    for col in range (0,n):
        curr = row+col+1
        if curr>n:
            curr = 2*n-curr
        print(str(curr) + " ", end="")
    print()
