#импорт всех функций математической библиотеки
from math import *
from statistics import *
import random 

# задание 1
print('Задание 1\n')

print("Вася\n      пошел\n                   гулять")

print(" ^     ^")
print("( o   o )")
print("    x    ")
print("/   L L")
print("/   )")
print("/  )")
print("L L")

question=input('Дать Васе рыбку? 1 - да, 0 - нет\n')
print("Ваш ответ: ", question)

if int(question) == 1:
    print(" ^     ^")
    print("( o   o )")
    print("    x         Спасибо!")
    print("/   L L ><>")
    print("/   )")
    print("/  )")
    print("L L")
else:
    print(" ^     ^")
    print("( >   < )")
    print("    x    ")
    print("/   L L ")
    print("/   )")
    print("/  )")
    print("L L")


print("Задача 2.1: ввести с клавиатуры три целых числа, найти их сумму, произведение и среднее арифметическое")
n1=input("Число 1: \n")
n2=input("Число 2: \n")
n3=input("Число 3: \n")
list_task2 = (int(n1), int(n2), int(n3))

print("Сумма = ", int(n1)+int(n2)+int(n3))
print("\nПроизведение = ", int(n1)*int(n2)*int(n3))
print("\nСреднее арифметическое = ", mean(list_task2))
print("\n")

print("Задача 2.2: ввести с клавиатуры координаты двух точек (A и B) на плоскости (вещественные числа). Вычислить длину отрезка AB\n")
print("Введите координаты точки A/n")
x1=input("x1: \n")
y1=input("y1: \n")
print("Введите координаты точки B/n")
x2=input("x2: \n")
y2=input("y2: \n")
print("Длина отрезка AB = ", abs(sqrt(pow(float(y2)-float(y1),2) + pow(float(x2)-float(x1),2))))

print("\nЗадача 2.3: Получить случайное трехзначное число и вывести через запятую его отдельные цифры\n")
n_rand=random.randint(100,999)
str_rand = str(n_rand)
list_rand = (str_rand)
print("Случайное число = " + str_rand + ". Eго отдельные цифры: ")
print(list_rand[0], list_rand[1], list_rand[2], sep = ',')

