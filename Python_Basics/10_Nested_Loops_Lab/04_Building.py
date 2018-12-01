import sys

floors = int(input())
rooms_per_floor = int(input())

for i in range(floors,0,-1):
    for j in range(0, rooms_per_floor):
        if i==floors:
            print(f'L{i}{j} ' , end="")
            sys.stdout.flush()
        elif i%2 == 0:
            print(f'O{i}{j} ', end="")
            sys.stdout.flush()
        else:
            print(f'A{i}{j} ', end="")
            sys.stdout.flush()
    print()