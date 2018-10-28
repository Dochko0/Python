import math

all_Steps = float(input())
dancers = float(input())
days_For_Learning = float(input())

steps_per_day = math.ceil(((all_Steps/days_For_Learning)/all_Steps)*100)
steps_per_dancer = steps_per_day/dancers

if steps_per_day<=13:
    print(f'Yes, they will succeed in that goal! {steps_per_dancer:.2f}%.')
else:
    print(f'No, They will not succeed in that goal! Required {steps_per_dancer:.2f}% steps to be learned per day.')