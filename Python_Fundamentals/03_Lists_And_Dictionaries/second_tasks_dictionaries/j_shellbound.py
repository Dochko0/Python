import math

town_shell = {}

while True:
    line = input().split()
    if line[0] == "Aggregate":
        break

    num = int(line[1])

    if line[0] not in town_shell:
        town_shell[line[0]] = []

    if num not in town_shell[line[0]]:
        town_shell[line[0]].append(num)

for x in town_shell:
    giant_shell = math.ceil(sum(town_shell[x]) - (sum(town_shell[x]) / len(town_shell[x])))
    print(f'{x} -> ', end="")
    print(", ".join(str(y) for y in town_shell[x]), end="")
    print(f' ({giant_shell})')

print()
