topic_dict = {}

while True:
    line = input().split(' -> ')
    if line[0] == 'filter':
        break

    topic = line[0]

    tags = line[1].split(', ')
    if topic not in topic_dict:
        topic_dict[topic] = []

    for z in tags:
        if z not in topic_dict[topic]:
            topic_dict[topic].append(z)

filter = input().split(', ')

for x in topic_dict:
    check = True
    for h in filter:
        if h not in topic_dict[x]:
            check= False
            break
    if check:
        print(f'{x} | #' + ', #'.join(y for y in topic_dict[x]))

