my_list = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт"}),
           (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт"}),
           (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт"})]

n = 3
i = int(input("Введите количество товаров, которые хотите довнести: "))
el = 1
while el <= i:
    name = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    col = int(input("Введите количество товара: "))
    ed = input("Введите наименование единиц: ")
    ls = (n + el, {"название": name, "цена": price, "количество": col, "ед": ed})
    my_list.append(ls)
    el += 1
print(my_list)

my_list_2 = []
count = 0
for i, v in my_list:
    my_list_2.append((my_list[count][1]).get("название"))
    count += 1
print(my_list_2)

my_list_3 = []
count = 0
for i, v in my_list:
    my_list_3.append((my_list[count][1]).get("цена"))
    count += 1
print(my_list_3)

my_list_4 = []
count = 0
for i, v in my_list:
    my_list_4.append((my_list[count][1]).get("количество"))
    count += 1
print(my_list_4)

my_list_5 = []
count = 0
for i, v in my_list:
    my_list_5.append((my_list[count][1]).get("ед"))
    count += 1
print(my_list_5)

my_dict = {"название": my_list_2,
           "цена": my_list_3,
           "количество": my_list_4,
           "ед": my_list_5}

print(my_dict)