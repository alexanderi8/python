print('Первое задание')
f_obj = open("my_file.txt", 'w')
while True:
    stroka = input('введите строку: ')
    if not stroka:
        break
    f_obj.write(stroka + '\n')
f_obj.close()
f_obj = open("my_file.txt", 'r')
for line in f_obj:
    print(line)
f_obj.close()

print('Второе задание')
lines = 0      # счетчик строк
n = 1          # нумерация
with open('task2.txt.txt', 'r') as my_file:
    for line in my_file:
        lines += 1
        words_line = line.split()
        print(f"Длина {n}-строки - {len(words_line)}")
        n += 1
print('Количество строк всего - ', lines)

print('Третье задание')
list_persons = []
list_salary = []
count = 0
with open('task3.txt.txt', 'r') as new_file:
    for line in new_file:
        person = line.split()
        list_salary.append(float(person[1]))
        count += 1
        if float(person[1]) > 20000:
            list_persons.append(person[0])
print('Зарплата более 20тыс. у следующих сотрудников: ', ", ".join(list_persons))
print(f'Средняя зарплата сотрудников - {sum(list_salary) / count:.2f}')

print('Четвертое задание')
new_list = []       # создаем пустой список
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть", "Seven": "Семь"}
with open('task4.txt.txt', 'r') as list_num:
    for line in list_num:          # добавляем в список значение по словарю если значение строки совпадает с ключом
        new_list.append(' '.join([my_dict.get(i, i) for i in line.split()]))  # если не сопадает добавляем исходное зн.
print(new_list)
with open('new_task4.txt', 'w') as new_file_task:
    for i in new_list:               # записываем построчно
        new_file_task.write(i + '\n')

print('Пятое задание')
with open('task5.txt', 'w') as file_numbers:
    file_numbers.write('7 2 12 8 34 21 47 5 3 6')
with open('task5.txt', 'r') as file_n:
    str_numbers = file_n.readline()     # записываем в переменую строку чисел
    suma = 0
    listn = str_numbers.split()   # из строки создаем список из чисел в строковом выражении
    for i in listn:        # вариант 1 пробежаться циклом по списку и посчитать сумму
        suma += int(i)
    print(suma)
    new_list = list(map(int, listn))     # вариант 2 получить список чисел и применить функцию sum
    print(sum(new_list))

print('Шестое задание')
my_dict = {}    # создаем пустой словарь
with open('task6.txt', 'r') as file_subj:
    for line in file_subj:
        res = line.replace('(', ' ').replace(': ', ' ').split() # меняем скобку и двоеточие на пробел, делим строку по пробелу
        data = [i for i in res if i.isdigit()]   # добавляем в список значение если оно является числом
        sum_el = sum(list(map(int, data)))       # вычисляем сумму чисел, конвертируя в int
        my_dict[res[0]] = sum_el                 # добавляем в словарь
print(my_dict)

print('Седьмое задание')
my_dict_firm = {}          # создаем три пустых словаря
aver_dict = {}
ubyt_firm = {}
suma_rev = 0               # сумма прибыли
count = 0                  # счетчик прибыльных фирм
with open('task7.txt', 'r') as file_firm:
    for line in file_firm:
        res_firm = line.split()
        if int(res_firm[2]) > int(res_firm[3]):           # если фирма прибыльная - добавляем след знач в словарь и выполняем подсчет
            my_dict_firm[res_firm[0]] = int(res_firm[2]) - int(res_firm[3])
            suma_rev += int(res_firm[2]) - int(res_firm[3])
            count += 1
        else:
            ubyt_firm[res_firm[0]] = int(res_firm[2]) - int(res_firm[3])       # иначе добавляем убыточные фирмы в словарь
aver_dict["average_profit"] = int(suma_rev / count)                            # подсчет средней прибыли
list_f = (f"Фирмы с прибылью - {my_dict_firm} \nСредняя прибыль - {aver_dict} \nФирмы с убытками - {ubyt_firm}")
print(list_f)
data_file = [my_dict_firm, aver_dict, ubyt_firm]
import json
with open('my_data_file.json', 'w') as data_write:
    json.dump(data_file, data_write)
    json_str = json.dumps(data_file)
    print(json_str)
    print(type(json_str))
