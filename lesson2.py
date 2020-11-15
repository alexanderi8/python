
print("Первое задание")
a = ["string", 13, 256.3, None]
for el in a:
    print(type(el))

print("Второе задание")
ls = []
c = int(input("Введите количество элементов списка: "))
d = 0
while d < c:
    ls.append(input("Введите элемент списка"))
    d += 1
print(ls)
print(len(ls))
i = 0
while i < (len(ls))-1:
    ls[i], ls[i+1] = ls[i+1], ls[i]
    i = i + 2
print(ls)

print("Третье задание")
num = int(input("Введите номер месяца: "))
num -= 1
months = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
print("Время года -", months[num])
month_dict = {"зима": (1, 2, 12), "весна": (3, 4, 5), "лето": (6, 7, 8), "осень": (9, 10, 11)}
num_1 = int(input("Введите номер месяца: "))
if num_1 < 1 or num_1 > 12:
    print("такого месяца нет")
for k, v in month_dict.items():
    if num_1 in v:
        print("Время года - ", k)

print("Четвертое задание")
stroka = input("Введите строку: ").split()
for ind, word in enumerate(stroka):
    ind += 1
    print(ind, "{:.10}".format(word))

print("Пятое задание")
my_list = [13, 11, 6, 4, 2]
num_2 = int(input("Введите рейтинг: "))
count = 0
for i in my_list:
    if num_2 <= i:
        count += 1
my_list.insert(count, num_2)
print(my_list)

