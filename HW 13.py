count = int(input("Kоличество билетов:  "))
age = [int(input("Возраст посетителя: ")) for i in range(count) ]
age_18 = [i for i in age if 18 <= i < 25]
age_25 = [i for i in age if i >= 25]
summa_tickets = len(age_18) * 990 + len(age_25) * 1390
if len(age) > 3:
    summa_tickets *= 0.9
print("Стоимость вашей покупки:", summa_tickets, "руб.")
