class Exercises:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = [*problems]

    def get_info(self):
        info = f'Exercises: {self.topic}\n' \
            f'Problems for exercises and homework for the "{self.course_name}" course @ SoftUni.' \
            f'\nCheck your solutions here: {self.judge_contest_link}\n'

        for p in range(len(self.problems)):
            if p == len(self.problems) - 1:
                info += f'{p + 1}. {self.problems[p]}'
            else:
                info += f'{p + 1}. {self.problems[p]}\n'
        return info


num = 1
items = []
while True:
    line_input = input()
    if line_input == 'go go go':
        break

    topic, course_name, judge_contest_link, all_problems = list(line_input.split(' -> '))
    problems = all_problems.split(', ')
    items.append(Exercises(topic, course_name, judge_contest_link, problems))

for i in items:
    print(i.get_info())



