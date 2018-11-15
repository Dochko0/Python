n = int(input())
under200 = 0
bt200to399 = 0
bt400to599 = 0
bt600to799 = 0
more800 = 0

for i in range(1, n+1):
    num = int(input())
    if num<200:
        under200+=1
    elif 200<=num<=399:
        bt200to399+=1
    elif 400<=num<=599:
        bt400to599+=1
    elif 600<=num<=799:
        bt600to799+=1
    else:
        more800+=1

percent_under200 = (under200/n) *100
percent_bt200to399 = (bt200to399/n) *100
percent_bt400to599 = (bt400to599/n) *100
percent_bt600to799 = (bt600to799/n) *100
percent_more800 = (more800/n) *100

print(f'{percent_under200:.2f}')
print(f'{percent_bt200to399:.2f}')
print(f'{percent_bt400to599:.2f}')
print(f'{percent_bt600to799:.2f}')
print(f'{percent_more800:.2f}')