num_list = list(map(int, input().split(" ")))
counter = 0

for i in num_list:
    if i%2!=0:
        counter+=1

print(counter)