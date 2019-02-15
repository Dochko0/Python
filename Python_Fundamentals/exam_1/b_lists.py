def average_sum(nums):
    average = sum(nums) / len(nums)
    return average


while True:
    words = input()
    if words == 'stop playing':
        break
    numbers = list(map(int, words.split()))

    if len(set(numbers)) == len(numbers):
        for i in range(0, len(numbers)):
            if numbers[i] % 2 == 0:
                numbers[i] += 2
        average = average_sum(numbers)
        numbers = sorted(numbers)
        print(f'Unique list: ' + ','.join(str(x) for x in numbers))
        print(f'Output: {average:.2f}')

    else:
        for i in range(0, len(numbers)):
            if numbers[i] % 2 != 0:
                numbers[i] += 3
        average = average_sum(numbers)
        numbers = sorted(numbers)
        print(f'Non-unique list: ' + ':'.join(str(x) for x in numbers))
        print(f'Output: {average:.2f}')
