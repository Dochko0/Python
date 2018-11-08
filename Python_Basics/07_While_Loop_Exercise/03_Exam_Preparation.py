bad_result_count = int(input())
count_bad = 0
count = 0
last_problem = ''
all_score = 0

while True:
    task = input()
    if task == 'Enough':
        break

    rating = float(input())
    if rating <= 4:
        count_bad += 1
        if count_bad == bad_result_count:
            print(f'You need a break, {bad_result_count} poor grades.')
            break

    count += 1
    last_problem = task
    all_score += rating

if count_bad != bad_result_count:
    average = all_score / count
    print(f'Average score: {average:.2f}')
    print(f'Number of problems: {count}')
    print(f'Last problem: {last_problem}')
