print("Первое задание")
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __add__(self, other):
        res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix)):
             for j in range(len(self.matrix[0])):
                 res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res)
    def __str__(self):
        return "\n".join("  ".join([str(item) for item in line]) for line in self.matrix)

matr1 = [[14, 2, 16], [13, 3, 15], [12, 14, 10]]
matr2 = [[2, 12, 17], [11, 14, 16], [15, 9, 8]]
my_1 = Matrix(matr1)
my_2 = Matrix(matr2)
print(my_1 + my_2)

print("Второе задание")
from abc import ABC, abstractmethod
class Wear(ABC):
    def __init__(self, param):
        self.param = param
    @property
    @abstractmethod
    def calc_tkani(self):
        pass
    def __add__(self, other):
        return self.calc_tkani + other.calc_tkani
class Palto(Wear):
    @property
    def calc_tkani(self):
        return (self.param / 6.5) + 0.5

class Costum(Wear):
    @property
    def calc_tkani(self):
        return (self.param * 2) + 0.3

my_c1 = Palto(44)
print(f"{my_c1.calc_tkani:.2f}")
my_c2 = Costum(1.75)
print(f"{my_c2.calc_tkani:.2f}")
print(f"Общий расход ткани - {my_c1 + my_c2:.2f}")

print("Третье задание")
class Cell:
    def __init__(self, cell):
        self.cell = cell
    def __add__(self, other):
        return self.cell + other.cell
    def __sub__(self,other):
        if self.cell - other.cell > 0:
            return self.cell - other.cell
        else:
            return "Невозможно произвести вычитание"
    def __mul__(self, other):
        return self.cell * other.cell
    def __truediv__(self, other):
        return self.cell // other.cell
    def make_order(self, row):
        c = self.cell
        os = self.cell % row
        while c // row > 0:
            print("o" * row)
            c -= row
        print("o" * os)
cell1 = Cell(35)
cell2 = Cell(6)
cell1.make_order(6)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 / cell2)