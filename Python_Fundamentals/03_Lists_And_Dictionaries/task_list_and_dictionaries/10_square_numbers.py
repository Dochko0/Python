import math

# line_list =[int(number) for number in input().split(' ') if int(number) > 0]

line_list = list(map(int, input().split()))
line_list = [x for x in line_list if x >= 0 and math.sqrt(x) == int(math.sqrt(x))]
# square_list = []

# for x in line_list:
#     if math.sqrt(x) == int(math.sqrt(x)):
#         square_list.append(x)

# square_list.sort(reverse=True)
line_list.sort(reverse=True)
# print(" ".join(str(x) for x in square_list))
print(" ".join(str(x) for x in line_list))





from math import sqrt

numbers = [int(number) for number in input().split(' ') if int(number) > 0]

squares = [x for x in numbers if (sqrt(x) == int(sqrt(x)))]
squares.sort(reverse=True)

result = ' '.join([str(number) for number in squares])

print(result)