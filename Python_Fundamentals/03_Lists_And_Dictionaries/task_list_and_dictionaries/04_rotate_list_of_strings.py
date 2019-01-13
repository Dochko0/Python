element_list = input().split(" ")
rotated_list = []

rotated_list.append(element_list[len(element_list) - 1])

for i in range(0, len(element_list) - 1):
    rotated_list.append(element_list[i])

print(" ".join(rotated_list))
