#Упражнение 110. Порядок сортировки
'''
spisok = []
x = int(input())
while x!=0:
    spisok.append(x)
    x = int(input())
spisok.sort()
print(spisok)
'''
#Упражнение 111. Обратный порядок
'''
spisok = []
x = int(input())
while x!=0:
    spisok.append(x)
    x = int(input())
spisok.sort()
print(spisok[::-1])
'''
#Упражнение 112. Удаляем выбросы
'''
def not_min_and_max(spisok1):
    new_spisok = []
    for i in spisok1:
        if i != max(spisok1) and i != min(spisok1):
            new_spisok.append(i)
    return new_spisok

spisok = []
x = int(input())
while x!=0:
    spisok.append(x)
    x = int(input())
if len(spisok)<4:
    print("Ошибка")
else:
    print(not_min_and_max(spisok))
'''
#Упражнение 113. Избавляемся от дубликатов
'''
spisok = []
x = input()
while x!='':
    spisok.append(x)
    x = input()
for i in range(len(spisok)):
    f=1
    for j in range(i):
        if spisok[i]==spisok[j]:
            f=0
            break
    if f:
        print(spisok[i])
'''
#Упражнение 114. Отрицательные, положительные и нули
'''
spisok = []
x = input()
while x!='':
    spisok.append(int(x))
    x = input()
for i in spisok:
    if i<0:
        print(i, end=' ')
for i in spisok:
    if i==0:
        print(i, end=' ')
for i in spisok:
    if i>0:
        print(i, end=' ')
'''
#Упражнение 115. Список собственных делителей
'''def count_del(x):
    spisok = []
    for i  in range(1, x):
        if x % i == 0:
            spisok.append(i)
    return spisok

n = int(input())
print(count_del(n))
'''
#Упражнение 116. Совершенные числа
'''
def count_del(x):
    spisok = []
    for i  in range(1, x):
        if x % i == 0:
            spisok.append(i)
    return spisok

def sov_num(x):
    spisok = count_del(x)
    return x == sum(spisok)

n = int(input())
print(sov_num(n))
'''
#Упражнение 117.Только слова
