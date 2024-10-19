list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_of_players = len(list_players)
middle = count_of_players // 2

first_team = list_players[:middle]
second_team = list_players[middle:]

print(first_team)
print(second_team)
