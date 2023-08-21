print("Задача 1.1: Ввести три целых числа, найти максимальное из них\n")
n1 = input("Введите число 1: ")
n2 = input("Введите число 2: ")
n3 = input("Введите число 3: ")
list_numbers = (int(n1),int(n2),int(n3))
print("Максимальное число = ", max(list_numbers))


print("Задача 1.2: Ввести пять целых числа, найти максимальное из них\n")
n1 = input("Введите число 1: ")
n2 = input("Введите число 2: ")
n3 = input("Введите число 3: ")
n4 = input("Введите число 4: ")
n5 = input("Введите число 5: ")
list_numbers = (int(n1),int(n2),int(n3),int(n4),int(n5))
print("Максимальное число = ", max(list_numbers))


print("Задача 1.3: Ввести последовательно возраст Антона, Бориса и Виктора. Определить, кто из них старше.\n")


a_name = "Антон"
b_name = "Борис"
v_name = "Виктор"

cont = 'y'

while cont=='y':
    a = input("Введите возраст Антона: ")
    b = input("Введите возраст Бориса: ")
    v = input("Введите возраст Виктора: ")

    if int(a)> int(b):
      if int(a)>int(v):
          print(a_name, " старше всех")
      elif int(a)==int(v):
          print(a_name,"и", v_name, " старше всех")
      elif int(a)<int(v):
          print(v_name, " старше всех")
    elif int(a)<=int(b):
       if int(a)==int(b) and int(v)>int(b):
           print(v_name, " старше всех")
       elif int(a)==int(b)==int(v):
           print("Джекпот")
       elif int(a)==int(b) and int(v)<int(b):
           print(a_name,"и", b_name, " старше всех")
       elif int(a)<int(b) and int(b)<int(v):
           print(v_name, " старше всех")
       elif int(a)<int(b) and int(b)>int(v):
           print(b_name, " старше всех")
    cont = input("Продолжить задавать возраст? y/n\n")

print("Задача 1.4: Напишите программу, которая получает три числа и выводит количество одинаковых чисел в этой цепочке.\n")

cont = 'y'
while cont=='y':
    
    n1 = input("Введите число 1: ")
    n2 = input("Введите число 2: ")
    n3 = input("Введите число 3: ")
    list_numbers = (int(n1),int(n2),int(n3))

    if list_numbers[0]==list_numbers[1]==list_numbers[2]:
        print("Все числа одинаковые")
    elif list_numbers[0]==list_numbers[2] and list_numbers[0]!=list_numbers[1]:
        print("Два числа одинаковые")
    else:
        print("Нет одинаковых чисел")

    cont = input("Продолжить проверять числа? y/n\n")


print("Задача 1.5: Напишите программу, которая получает номер месяца и выводит соответствующее ему время года или сообщение об ошибке.\n")

n1 = input("Введите номер месяца: ")
if int(n1) in range(1,12):
    if 3<=int(n1)<=5:
        print("Весна")
    elif 6<=int(n1)<=8:
        print("Лето")
    elif 9<=int(n1)<=11:
        print("Осень")
    else:
        print("Зима")
else:
    print("В году 12 месяцев, а не ", n1)


