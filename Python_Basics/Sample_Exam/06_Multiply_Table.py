num = input()[::-1]

num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])

for i in range(1,num1+1):
    for j in range(1,num2+1):
        for k in range(1,num3+1):
            result = i*j*k
            print(f'{i} * {j} * {k} = {result};')


