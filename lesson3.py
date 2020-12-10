
print("Первое задание")
def div_1():
    try:
        arg1 = float(input("Введите первое число: "))
        arg2 = float(input("Введите второе число: "))
        return print(arg1 / arg2)
    except ZeroDivisionError:
        return print("Error")

div_1()

print("Второе задание")
def user_info(name, sname, year, city, email, phone):
    print(f"name - {name}; sname - {sname}; year - {year}; city - {city}; email - {email}; phone - {phone}")
user_info(name="Gus", sname="Hidink", year=1946, city="Amsterdam", email="gus@gmail.com", phone="+538324910")

print("Третье задание")
def my_func(a, b, c):
    if b > a < c:
        return print(b + c)
    elif a > b < c:
        return print(a + c)
    else:
        return print(a + b)
my_func(20, 15, 30)

print("Четвертое задание")
def my_finc1(x, y):
    y = abs(y)
    return print(1 / (x ** y))
my_finc1(2,-3)

def my_func_2(a, b):
    b = abs(b)
    r = 1;
    while b > 0:
        r *= a
        b -= 1
    return print(1 / r)
my_func_2(2,-3)

print("Пятое задание")
suma = 0
while True:
    a = input("Введите строку чисел через пробел(нажмите f для выхода): ")
    ls = a.split(" ")
    ls_1 = []
    if "f" in ls: #специальный символ f
        for i in ls:
            if i != "f":
                ls_1.append(i)
        res = list(map(int, ls_1))
        suma = suma + sum(res)
        print("Сумма чисел равна - ", suma)
        print("Выход")
        break
    res = list(map(int, ls))
    suma = suma + sum(res)
    print("Сумма чисел равна - ", suma)

print("Шестое задание")
def int_func(str1):
    return str1.title()

str2 = input("Введите строку: ")
ls = str2.split(" ")
ls1 = []
for i in ls:
    ls1.append(int_func(i))
print(" ".join(ls1))