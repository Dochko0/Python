import sys

n = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize


for i in range(1,n+1):
    num = float(input())
    if i%2 == 0:
        even_sum+=num
        if even_max<=num:
            even_max=num
        if even_min>=num:
            even_min=num
    else:
        odd_sum += num
        if odd_max <= num:
            odd_max = num
        if odd_min >= num:
            odd_min = num

if odd_sum == 0 and even_sum==0:
    print(f'OddSum={odd_sum}, OddMin=No, OddMax=No, EvenSum={even_sum}, EvenMin=No, EvenMax=No')
elif even_sum==0:
    print(f'OddSum={odd_sum:.0f}, OddMin={odd_min:.0f}, OddMax={odd_max:.0f}, EvenSum={even_sum:.0f}, EvenMin=No , EvenMax=No')
elif odd_sum==0:
    print(f'OddSum={odd_sum:.0f}, OddMin=No, OddMax=No, EvenSum={even_sum:.0f}, EvenMin={even_min:.0f}, EvenMax={even_max:.0f}')
else:
    print(f'OddSum={odd_sum:.0f}, OddMin={odd_min:.0f}, OddMax={odd_max:.0f}, EvenSum={even_sum:.0f}, EvenMin={even_min:.0f}, EvenMax={even_max:.0f}')
