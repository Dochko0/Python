line = input()
dict={}

for x in line:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1

for key,value in dict.items():
    print(f'{key} -> {value}')
