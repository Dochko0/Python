import math

type_of_year = input()
count_holidays = int(input())
weekends_in_home = int(input())

weekends_in_sofia = 48 - weekends_in_home
games_home = weekends_in_home
games_weekends = weekends_in_sofia * 0.75
games_holidays = count_holidays * (2 / 3)
all_games = games_home + games_weekends + games_holidays
if type_of_year == "leap":
    all_games = all_games * 1.15
    print(math.floor(all_games))
else:
    print(math.floor(all_games))
