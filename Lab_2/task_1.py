money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
t=-1# -1 так как последний месяц, когда уже будет долг цикл будет считать как месяц без долга, т.к мы с начала прибавляем t+=1 а потом уже проверяем остаток
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital > 0:
    money_capital=money_capital - spend
    spend = spend+spend*increase
    money_capital=money_capital+salary
    t+=1
print("Количество месяцев, которое можно протянуть без долгов:", t)