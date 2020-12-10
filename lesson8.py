print("Первое задание")
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"день - {self.day}, месяц -  {self.month}, год - {self.year}"
    @classmethod
    def integ_data(cls, data):
        list_d = list(map(int, data.split("-")))
        day, month, year = list_d
        return cls(day, month, year)
    @staticmethod
    def correct_date(obj):
        if obj.day > 31 or obj.day < 1:
            return "Некорректный день"
        elif obj.month > 12 or obj.month < 1:
            return "Некорректный месяц"
        elif obj.year > 9999:
            return "Некорректный год"
        else:
            return "Корректная дата"
my_data = "10-12-2020"
my_1 = Date.integ_data(my_data)
print(my_1)
print(Date.correct_date(my_1))

print("Второе задание")
class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
num_1 = input("Введите числитель: ")
num_2 = input("Введите знаменатель: ")
try:
    int_num_1 = int(num_1)
    int_num_2 = int(num_2)
    if int_num_2 == 0:
        raise MyOwnError("Делить на ноль нельзя!")
except(ValueError, MyOwnError) as err:
    print(err)
else:
    print(int_num_1 / int_num_2)
finally:
    print("Завершение программы")
print("Третье задание")
# Не смог применить собственный класс исключение
class MyOwnError1(Exception):
     def __init__(self, txt):
         self.txt = txt
ls = []
while True:
    try:
        i = input("Введите число (для выхода нажмите 'stop'): ")
        if i == "stop":
            break
        i = int(i)
        ls.append(i)
    except ValueError:
        print("Вы ввели не число!")
print(ls)

# Задание 4-6 не осилил

print("Седьмое задание")
class Complex_num:
    def __init__(self, comp):
        self.comp = comp
    def __add__(self, other):
        return self.comp + other.comp
    def __mul__(self, other):
        return self.comp * other.comp

com_1 = Complex_num(3 + 5j)
com_2 = Complex_num(2 + 4j)
print(com_1 + com_2)
print(com_1 * com_2)