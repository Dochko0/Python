passengers_start = int(input())
stops = int(input())
curr_stop = 0

while True:
    if stops == curr_stop:
        break
    curr_stop += 1
    passengers_off = int(input())
    passengers_in = int(input())

    if curr_stop % 2 != 0:
        passengers_start = passengers_start - passengers_off + passengers_in + 2
    else:
        passengers_start = passengers_start - passengers_off + passengers_in - 2

print(f'The final number of passengers is : {passengers_start}')
