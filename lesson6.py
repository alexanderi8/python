print('Первое задание')
from itertools import cycle
import time
import colorama
from colorama import Fore, Style
colorama.init()
class TrafficLight:
    __color = ["Red", "Yellow", "Green", "Yellow"]
    def running(self):
        count = 0
        for i in cycle(self.__color):
            if count < 3:
                if i == "Red":
                    print(Fore.RED + 'Красный!')
                    time.sleep(7)
                    count += 1
                elif i == "Yellow":
                    print(Fore.YELLOW + "Желтый!")
                    time.sleep(2)
                elif i == "Green":
                    print(Fore.GREEN + "Зелёный!")
                    time.sleep(5)
            else:
                break
svet = TrafficLight()
svet.running()
print(Style.RESET_ALL)
print('Второе задание')
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def massa(self):
        return f"Масса полотна {(self._length * self._width * 25 * 5) / 1000} т"

polotno = Road(5000, 20)
print(polotno.massa())

print('Третье задание')
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f"Имя - {self.name}, Фамилия - {self.surname}")
    def get_total_income(self):
        print("Общий доход - ", sum(self._income.values()))

obj = Position("Mohhamed", "Salah", "Forward", 12000, 4500)
obj.get_full_name()
obj.get_total_income()

print('Четвертое задание')
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("Car is go")
    def stop(self):
        print("Car is stopped")
    def turn(self, direction):
        print(f"Car go {direction}")
    def show_speed(self):
        print("you speed - ", self.speed)
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Overspeed!!!")
        else:
            print("you speed - ", self.speed)
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Overspeed!!!")
        else:
            print("you speed - ", self.speed)
class PoliceCar(Car):
    pass
my_car = TownCar(65, "green", "Ford", False)
my_car.show_speed()
my_car1 = WorkCar(50, "yellow", "JCB", False)
my_car1.show_speed()
my_car2 = SportCar(100, "red", "Ferrari", False)
my_car2.show_speed()
print(my_car2.name)
print(my_car2.color)
my_car2.turn("right")
my_car3 = PoliceCar(70, "blue", "Honda", True)
print(my_car3.is_police)

print("Пятое задание")
class Stationery:
    def __init__(self, tutle):
        self.tutle = tutle
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
        print("Рисует ручка")
class Pencil(Stationery):
    def draw(self):
        print("Рисует карандаш")
class Handle(Stationery):
    def draw(self):
        print("Рисует маркер")
my_pen = Pen("Pen")
my_pen.draw()
my_pencil = Pencil("Pencil")
my_pencil.draw()
my_handle = Handle("Handle")
my_handle.draw()