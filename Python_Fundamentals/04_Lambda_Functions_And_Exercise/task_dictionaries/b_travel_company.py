city_dict = {}

while True:
    line = input().split(':')
    if line[0] == 'ready':
        break

    city = line[0]
    transport_line = line[1].split(',')

    if city not in city_dict:
        city_dict[city] = {}

    for transport in transport_line:
        vehicle, people = transport.split('-')
        city_dict[city][vehicle] = people

while True:
    city, accomodate = input().split()
    if city + ' ' + accomodate == 'travel time!':
        break
    accomodate = int(accomodate)
    people_sum = 0

    if city in city_dict:
        people_sum = sum(int(city_dict[city][x]) for x in city_dict[city])
        if accomodate < people_sum:
            print(f'{city} -> all {accomodate} accommodated')
        else:
            exept = accomodate - people_sum
            print(f'{city} -> all except {exept} accommodated')
