print("Первое задание")
from sys import argv
script_name, hours, stavka, premia = argv
print("Имя скрипта: ", script_name)
print("Количество отработанных часов: ", hours)
print("Ставка: ", stavka)
print("Премия: ", premia)

print((float(hours) * float(stavka)) + float(premia))

print("Второе задание")
my_list = [11, 2, 34, 3, 2, 5, 8, 67, 25, 11, 9, 2, 4]
new_list = [my_list[ind] for ind in range(1, len(my_list)) if my_list[ind] > my_list[ind - 1]]
print(new_list)              # берем значение по индексу и сравниваем его предыдущим значение начиная с индекс 1

print("Третье задание")
my_list1 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(my_list1)

print("Четвертое задание")
my_list3 = [2, 3, 4, 5, 5, 3, 1, 3, 2, 5, 6, 8, 9]
new_list = [my_list3[ind] for ind in range(len(my_list3)) if my_list3[ind] not in my_list3[ind + 1:] and my_list3[ind] not in my_list3[:ind - 1]]
print(new_list)        # берем значение по индексу добавляем его в новый список если нет такого же значения выше по списку и ниже по списку

print("Пятое задание")
from functools import reduce
new_mylist = [el for el in range(100, 1001) if el % 2 == 0]    # создаем список четных чисел
mult_all = reduce(lambda a, b: a * b, new_mylist)              # перемножаем список четных чисел
print(mult_all)

print("Шестое задание")
from itertools import count
for el in count(5):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle
count = 1
for i in cycle('ABC'):
    if count > 5:
        break
    print(i)
    count += 1

print("Седьмое задание")
def fact(n):
    fact_num = 1
    for i in range(1, n + 1):     # функция реализует подсчет факториала поочередно от 1 до n
        fact_num *= i
        yield (f"{i}! = {fact_num}")
n = int(input("Введите число: "))
print(fact(n))
for el in fact(n):                # с помощью цикла получаем выводим значение факториала от 1 до n
    print(el)