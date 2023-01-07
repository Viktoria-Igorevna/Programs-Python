per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Сумма под проценты:"))
deposit = list(per_cent.values()).copy()
for i in range(len(deposit)):
    deposit[i] *= (money/100)
    deposit[i] = int(deposit[i])
print("Накопленные средства за год:", deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))
