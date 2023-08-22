from math import *
from statistics import *

def CheckSymbol(symbol):
    res='?'
    str_numbers="1234567890"
    str_letters_lower="qwertyuioplkjhgfdsazxcvbnmйцукенгшщзхждлорпавыфячсмитьбю"
    str_letters_upper=str_letters_lower.upper()
    check=-1
    if check!=str_numbers.find(symbol):
        res='n'
    elif check!=str_letters_lower.find(symbol) or check!=str_letters_upper.find(symbol):
        res='l'
    else:
        res='s'
    return res

cont = 'y'
while cont=='y':
    task_number = input("Введите номер задачи 1-4: ")

    if int(task_number)==1:
        print("Задача 1: Реализовать калькулятор Вводятся 2 любых вещественных числа в переменные a и b. Необходимо вывести на экран меню с пунктами:\n")
        s_list = "1) a + b"
        d_list = "2) a - b"
        m_list = "3) a * b"
        div_list = "4) a / b"
        ost_list = "5) a % b"
        all_list = s_list+d_list+m_list+div_list+ost_list
        print(s_list, d_list, m_list, div_list, ost_list, sep = '\n')
        a = input("Введите a: ")
        b = input("Введите b: ")
        p_menu = input("Выберите пункт меню (1/2/3/4/5): ")
        #выбираем подстроку из пунктов меню
        n_list_start = int(all_list.find(p_menu))+3
        n_list_end = int(n_list_start)+5
        str_t = all_list[n_list_start:n_list_end] #промежуточная подстрока
        list_res = list(str_t)#переводим подстроку в список
        list_res[0]=a #заменяем a на введенное значение
        list_res[4]=b #заменяем b на введенное значение
        str_res=''
        for i in range(len(list_res)): #читаем из списка в итоговую подстроку
            str_res+=list_res[i]

        #говорят, eval() опасная штука, но тут ничего сломаться не должно
        if (p_menu=='4' or p_menu=='5') and int(b)==0:
            print("Вы пытались поделить на 0")
        else:
            print("Результат = ", eval(str_res))

    elif int(task_number)==2:
        print("Задача 2: Ввести с клавиатуры символ. Определить, чем он является: цифрой, буквой или знаком пунктуации")
        symbol = input("Введите символ: ")

        if len(symbol)>1:
            print("Нужен один символ")
        elif len(symbol)==0:
            print("Нужно ввести символ")
        else:
            if CheckSymbol(symbol)=='n':
                print("Это число")
            elif CheckSymbol(symbol)=='l':
                print("Это буква")
            elif CheckSymbol(symbol)=='s':
                print("Это символ")

    elif int(task_number)==3:
        print("Задача 3: Ввести с клавиатуры число и проверить, принадлежит ли это число диапазону от N до M включительно")
        number = input("Введите число: ")
        number = float(number)
        n = input("Введите левую границу N: ")
        n = float(n)
        m = input("Введите правую границу M: ")
        m = float(m)
        if n<=number<=m:
            print("Число принадлежит введенному диапазону")
        else:
            print("Число не принадлежит введенному диапазону")

    elif int(task_number)==4:
        print("Задача 4: Ввести с клавиатуры число и определить, является ли оно палиндромом")
        number=input("Введите число: ")
        number_list = list(number)
        number_list_rev=number_list.copy()
        number_list_rev.reverse()
        count=0
        for i in range(len(number_list)):
            if number_list[i]==number_list_rev[i]:
                count+=1
        if count == len(number_list):
            print('Число является палиндромом')
        else:
            print('Число не является палиндромом')

    cont=input("Повторить выбор задачи? y\n")
