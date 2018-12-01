num = int(input())
isHave = False

for i in range(1, 31):
    for j in range(1, 31):
        for k in range(1, 31):
            if i < j < k:
                sum = i + j + k
                if sum == num:
                    print(f'{i} + {j} + {k} = {sum}')
                    isHave=True
            if i > j > k:
                sum = i * j * k
                if sum == num:
                    print(f'{i} * {j} * {k} = {sum}')
                    isHave=True
if not isHave:
    print('No!')

# for i in range(3, num+1):
#     for j in range(2, num):
#         if j > i:
#             continue
#         for k in range(1, num - 1):
#             if i > j > k:
#                 sum = i * j * k
#                 if sum == num:
#                     print(f'{i} * {j} * {k} = {sum}')