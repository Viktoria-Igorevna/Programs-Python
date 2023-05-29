import random
import math
# Упражнение 85. Вычисляем длину гипотенузы
'''
def hypoteuse(kat1, kat2):
    return math.sqrt(kat1**2+kat2**2)

print("Введите катеты:")
katet_1,  katet_2 = float(input()), float(input())
print('Гипотенуза:', round(hypoteuse(katet_1,katet_2),2))
'''
# Упражнение 86. Плата за такси
'''
base_prise = 4.0
price = 0.25
def Taxi(len_km):
    len_m = len_km*1000
    return base_prise + price*(len_m//140)

len_km = float(input("Введите километраж Вашей поездки в км: "))
print("Стоимость вашей поездки: ", Taxi(len_km), "$", sep='')
'''
# Упражнение 87. Расчет стоимости доставки
'''
base_prise = 10.95
price = 2.95
def Delivery(count):
    return base_prise + price*(count - 1)

count_item = int(input("Количество позиций в заказе: "))
print("Стоимость Вашей доставки: ", Delivery(count_item),  '$', sep='')
'''
# Упражнение 88. Медиана трех значений
'''
def median(num1, num2, num3):
    spisok = [num1, num2, num3]
    spisok.sort()
    return spisok[1]

print("Введите 3 числа: ")
num_1, num_2, num_3 = int(input()), int(input()), int(input())
print("Медиана:", median(num_1, num_2, num_3))
'''
# Упражнение 89. Переводим целые числа в числительные
""""
numeral = {1:'one', 2:'two', 3:'three', 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",
           9:"nine", 10:"ten", 11:"eleven", 12:"twelve" }
def numeral_str(num):
    return numeral.get(num)

for i in range(1,13):
    print(i, '-', numeral_str(i))
"""
# Упражнение 90. Двенадцать дней Рождества
'''
numeral = {1:'first', 2:'second', 3:'third', 4:"fourth", 5:"fifth", 6:"sixth", 7:"seventh", 8:"eighth",
           9:"nineth", 10:"tenth", 11:"eleventh", 12:"twelfth"}
spisok = ["And a partridge in a pear tree\n",  "Two turtle doves\n", "Three French hens\n",
          "Four calling birds\n", "Five golden rings\n", "Six geese a–laying\n","Seven swans a–swimming\n",
          "Eight maids a–milking\n", "Nine ladies dancing\n", "Ten lords a–leaping\n", "Eleven pipers piping\n",
          "Twelve drummers drumming\n"]

def numeral_str(day):
    print(" On the " + numeral.get(day) + " day of Christmas\n"+" my true love sent to me:\n", *spisok[day-1::-1])

for i in range(1,13):
    numeral_str(i)
'''
# Упражнение 91. Григорианский календарь в порядковый
"""
years_ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
years_v = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def ordinalDate(day, month, years):
    if years % 100 == 0 and years % 400 == 0:
        return sum(years_v[:month-1])+day
    elif years % 4 == 0:
        return sum(years_v[:month - 1]) + day

    else:
        return sum(years_[:month-1])+day

to_day, to_month, to_years = int(input("День: ")), int(input("Месяц: ")), int(input("Год: "))
print(ordinalDate(to_day, to_month, to_years))
"""
# Упражнение 92. Порядковая дата в григорианский календарь
"""
years_ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
years_v = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def ordinalDate(day, month, years, days=90):
    years_t = ""
    if years % 100 == 0 and years % 400 == 0:
        len_ = sum(years_v[:month - 1]) + day + days
        years_t ="V"
    elif years % 4 == 0:
        len_ = sum(years_v[:month - 1]) + day + days
        years_t = "V"
    else:
        len_ = sum(years_[:month - 1]) + day + days
    month_i = 0
    if years_t:
        if len_ > 366:
            len_ -=366
            years += 1
    else:
        if len_ > 365:
            len_ -= 365
            years += 1
    while len_ - years_[month_i] > 0:
        if years_t:
            len_ -= years_[month_i]
        else:
            len_ -= years_[month_i]
        month_i += 1
    return len_, month_i+1, years


to_day, to_month, to_years = int(input("День: ")), int(input("Месяц: ")), int(input("Год: "))
day = ordinalDate(to_day, to_month, to_years, 90)
print('------------')
print("День:", day[0])
print("Месяц:", day[1])
print("Год:", day[2])
"""
# Упражнение 93. Центрируем строку
""""
def Center_str(s, w):
    if len(s) >= w:
        print(s)
    else:
        print(' ' * ((w - len(s)) // 2) + s)

stroka = input("Введите сторку: ")
width_1 = int(input("Ширина строки: "))
print("Результат: ")
print(' ' * width_1, '|')
Center_str(stroka, width_1)
"""
# Упражнение 94. Треугольник ли?
""""
def triangle(side_1, side_2, side_3):
    sum_1_2 = side_1 + side_2
    sum_2_3 = side_2 + side_3
    sum_1_3 = side_1 + side_3
    return side_1 and side_2 and side_3 and (side_1 < sum_2_3 and side_2 < sum_1_3 and side_3 < sum_1_2)

s_tr1, s_tr2, s_tr3 = int(input("Сторона 1: ")), int(input("Сторона 2: ")), int(input("Сторона 3: "))
print('Является ли треугольником?', triangle(s_tr1, s_tr2, s_tr3))
"""
# Упражнение 95. Озаглавим буквы
"""
punctuation_marks = [".", '?', "!"]
def headline_letters(stroka):
    f = False
    i = 0
    while stroka[i] == ' ' and i < len(stroka)-1:
        i += 1
    new_stroka = ' ' * i +stroka[i].upper()
    i += 1
    while i < len(stroka)-2:
        if stroka[i] == 'i' and (stroka[i+1] == ' ' or stroka[i+1] == "’"):
            new_stroka += stroka[i].upper()
            i += 1
        elif stroka[i] in punctuation_marks:
            new_stroka += stroka[i:i+2]
            new_stroka += stroka[i+2].upper()
            i += 3
        else:
            new_stroka += stroka[i]
            i += 1
    if stroka[i] == 'i':
        return new_stroka + stroka[i].upper() + stroka[i+1:]
    else:
        return new_stroka + stroka[i:]

stroka = input("")
print(headline_letters(stroka))
"""
# Упражнение 96. Является ли строка целым числом?
"""
num = '1234567890'
def isInteger(stroka):
    f = True
    new_stroka = stroka.strip(' ')
    for i in new_stroka:
        if i not in '1234567890':
            f = False
            break
    return f
stroka = input("Введите строку: ")
print('Является ли строка, целым числом?',isInteger(stroka))
"""
# Упражнение 97. Приоритеты операторов
"""
def precedence(operator):
    if operator in "+-":
        return 1
    elif operator in "*/":
        return 2
    elif operator == "^":
        return  3
    else:
        return -1
you_operator = input("Введите обозначение оператора: ")
print("Приоритет:", precedence(you_operator))
"""
# Упражнение 98. Простое число?
""""
def simple_num(num):
    Simple = False
    for i in range(2, num):
        if num % i == 0:
            Simple = False
            break
    return Simple

you_num = int(input("Введите число: "))
if simple_num((you_num)):
    print("Число не простое")
else:
    print("Число простое")
"""
# Упражнение 99. Следующее простое число
"""
def nextPrime(n):
    num = n + 1
    while True:
        Simple = True
        for i in range(2,num):
            if num % i == 0:
                Simple = False
                break
        if Simple:
            break
        else:
            num += 1
    return num

you_num = int(input("Введите число: "))
print("Следующее простое число:", nextPrime((you_num)))
"""
# Упражнения 103. Cозданиен случайного надежного пароля
""""
numbers = '0123456789'
capital_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_let = 'abcdefghijklmnopqrstuvwxyz'

def randomPassword():                   # Создание пароля
    lenght_pass = random.randint(7, 10)
    new_pass = ""
    for i in range(lenght_pass):
        element = random.randint(33, 126)
        new_pass += chr(element)
    return new_pass

def passwordCheck(passw):               # Проверка на недежность
    criterion_1 = False
    criterion_2 = False
    criterion_3 = False
    criterion_4 = False
    if len(passw)>=8:
        criterion_1 = True
    for i in passw:
        if i in numbers:
            criterion_2 = True
        elif i in capital_let:
            criterion_3 = True
        elif i in lower_let:
            criterion_4 = True
    return criterion_1 and criterion_2 and criterion_3 and criterion_4

password = randomPassword()
count = 1
while not(passwordCheck(password)):
    password = randomPassword()
    count += 1
print("Надежный пароль с",count, 'попытки:', password)
"""
#Упражнение 101. Случайный номерной знак
"""
def randomLicensePlate():
    new_or_old = random.randint(0,1)
    new_plate = ""
    if new_or_old:
        for i in range(3):
            element = random.randint(65, 90)
            new_plate += chr(element)
        for i in range(3):
            element = random.randint(0, 1)
            new_plate += str(element)
    else:
        for i in range(4):
            element = random.randint(0, 1)
            new_plate += str(element)
        for i in range(3):
            element = random.randint(65, 90)
            new_plate += chr(element)
    return new_plate

print("Номерной знак:", randomLicensePlate())
"""
#Упражнение 105. Перевод в произвольные системы счисления
'''
ten = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
def hex2int(char_):
    for i in ten.keys():
        if char_ == i:
            return ten.get(i)

def numberSystems(from_system, in_system, num):
    if from_system == 10:
        return from10System(in_system, num)
    elif in_system == 10:
        return in10System(from_system, num)
    else:
        return from10System(in_system,in10System(from_system, num))

def in10System(system, num):
    result = 0
    for i in range(len(num)):
        result += hex2int(num[i]) * system ** (len(num) - i-1)

    return result

def from10System(system, num):
    result =''
    num = int(num)
    while num // system!=0:
        result += str(num % system)
        num //= system
    result += str(num % system)
    return result[::-1]

print(numberSystems(5, 8,'123'))
'''
#Упражнение 106. Дни в месяце
""""
def countDays(month, years):
    if month == 2:
        if years % 100 == 0 and years % 400 == 0: return 29
        elif years % 4 == 0: return 29
        else: return 28
    else:
        if month in [1,3,5,7,8,10, 12]:
            return 31
        else:
            return 30
"""
#Упражнение 107. Максимальное сокращение дробей
'''
def max_del1(a, b):
    del_=0
    if a>b:
        for i in range(2, b+1):
            if a%i==0 and b%i==0:
                del_= i
    else:
        for i in range(2, a+1):
            if a%i==0 and b%i==0:
                del_ = i
    return a//del_, b//del_

print(max_del1(6,63))
'''
#Упражнение 108. Переводим меры
'''
def perevod(a,b):
    if b == 'teaspoons':
        cup = a // 48
        tablespoons = a % 48 // 3
        teaspoons = a % 3
    else:
        cup = a // 16
        tablespoons = a % 16
    s = ''
    if cup==1:
        s = s + str(cup) + ' cup'
    elif cup >1:
        s = s + str(cup) + ' cups'
    if tablespoons==1:
        s = s + ' ' + str(tablespoons) + ' tablespoon'
    elif tablespoons >1:
        s = s + ' ' + str(tablespoons) + ' tablespoons'
    if teaspoons==1:
        s = s +' ' +  str(teaspoons) + ' teaspoon'
    elif teaspoons >1:
        s = s + ' ' + str(teaspoons) + ' teaspoons'
    return s
print(perevod(59, 'teaspoons'))


'''
#Упражнение 109. Магические даты
'''
def magic_data(day, month, year):
    return day*month == year % 100

print(magic_data(10,6,1961))
'''







