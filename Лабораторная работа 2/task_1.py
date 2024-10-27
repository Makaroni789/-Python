money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

day_count = 0

while money_capital > 0:
    money_capital += salary
    new_spend = spend * ((1 + increase) ** day_count)
    if money_capital - new_spend <= 0:
        break
    money_capital -= new_spend
    day_count += 1

print("Количество месяцев, которое можно протянуть без долгов:", day_count)
