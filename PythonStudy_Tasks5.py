
from math import *
from statistics import *
from functions import Upyachka as U
from functions import KorolIShut as K


    

cont = 'y'
while cont=='y':
    task_number = input("Введите номер задачи 1-5: ")

    if int(task_number)==1:
        print("Задача 1: Определить, параллельна ли определенная прямая линия оси ординат, либо оси абсцисс. Прямая задается двумя точками")
        ax = input("Введите координату Ax: ")
        ay = input("Введите координату Ay: ")
        bx = input("Введите точку Bx: ")
        by = input("Введите точку By: ")
        #проверяем, что введенные значения - числа
        try:
            ax=float(ax)
            ay=float(ay)
            bx=float(bx)
            by=float(by)
        except ValueError:
            print("Введите числа")
        else:
            if ax==bx and ay==by:
                print("Это точка")
            elif ax==bx==0:
                print("Прямая совпадает с осью Y")
            elif ay==by==0:
                print("Прямая совпадает с осью X")
            else:
                a_arr=[ax,ay]
                b_arr=[bx,by]
                if ay==by:
                    print("Прямая параллельная оси X")
                elif ax==bx:
                    print("Прямая параллельная оси Y")
                else:
                    print("Прямая не параллельная ни одной оси")

       

    elif int(task_number)==2:
        print("Задача 2: Ввести с клавиатуры шестизначный номер билета и определить, является ли он счастливым")
        num = input("Введите номер билета из 6 цифр: ")
        try:
            num=int(num)
        except ValueError:
            print("Введите числа")
        else:
            num=str(num)
            if len(num)!=6 and num!='0':
                print("Введите 6 цифр")
            elif num=='0':
                print("Свежий билетик, наверное, еще теплый:)")
            else:
                num1 = num[:3]
                num2 = num[3:]
                sum_num1 = int(num1[0])+int(num1[1])+int(num1[2])
                sum_num2 = int(num2[0])+int(num2[1])+int(num2[2])
                if sum_num1 == sum_num2:
                    print("Билет счастливый")
                else:
                    print("Обычный билет")
        

    elif int(task_number)==3:
        print("Задача 3: Указать с клавиатуры пол и возраст человека. Определить, пора ли ему на пенсию")
        sex = input("Введите пол: ")
        age = input("Введите возраст: ")
        s_list = ['M','М','м','m','F','f','Ж','ж']
        as_dict = {s_list[0]:65, s_list[1]:65,s_list[2]:65, s_list[3]:65,s_list[4]:60, s_list[5]:60,s_list[6]:60, s_list[7]:60}
        # добавить функцию для проверки возраста на принадлежность к числу
        s_ok = 0
        for i in range(len(s_list)):
            if s_list[i]==sex:
                s_ok+=1
        if s_ok == 0:
            print("У нас так не принято")
        else:
            i==0
            for i in range(len(s_list)):
                if s_list[i]==sex:
                    if int(as_dict[s_list[i]]) < int(age):
                        print("Вы достигли пенсионного возраста")
                    else:
                        print("Пока рано на пенсию")


    elif int(task_number)==4:
        print("Задача 4: Написать программу, которая предлагает пользователю выбрать животное из списка и в ответ показывает, какие звуки издает выбранное животное")

        file = open('animals.txt',mode='r',encoding='utf-8')
        content_animals = file.read()
        print("Список животных:\n", content_animals)
        file.close()

        file = open('voices.txt',mode='r',encoding='utf-8')
        content_voices = file.read()
     #       print(content_voices)
        file.close()
        n_animal = input("Выберите животное (цифру пункта меню): ")
        try:
            n_animal = int(n_animal) - 1
        except ValueError:
            print("Вы ввели не число")
        else:
            l_animals=list()
            l_voices=list()
            l_animals = content_animals.split('\n')
            l_voices = content_voices.split('\n')
   #         print(l_animals)
   #         print(l_voices)
            l_res=''
            for i in range(len(l_animals)):
   #             print("i = ", i)
                tmp_animals = l_animals[i]
                if i<9:
                    tmp_animals = tmp_animals[:3]
   #                 print("tmp_animals: ", tmp_animals, "length: ", len(tmp_animals), " ", i, " ", n_animal)
                else:
                    tmp_animals = tmp_animals[:4]
   #                 print("tmp_animals: ", tmp_animals, "length: ", len(tmp_animals), " ", i, " ", n_animal)

                for j in range(len(l_voices)):
                    tmp_voices = l_voices[j]
                    if i<9:
                        tmp_voices = tmp_voices[:3]
   #                     print("tmp_voices: ", tmp_voices, "length: ", len(tmp_voices)," ", j, " ", n_animal)
                    else:
                        tmp_voices = tmp_voices[:4]
   #                     print("tmp_voices: ", tmp_voices, "length: ", len(tmp_voices), " ", j, " ", n_animal)
   #                 if (l_animals[i]==l_voices[j] or l_animals[i]==l_voices[j-1]) and n_animal==i:
                    if tmp_animals==tmp_voices and n_animal==i:
                        l_res+=l_voices[j].replace(tmp_voices,'')
                        l_res+='\n'

            print(l_res)

    elif int(task_number)==5:
        print('Задача 5: Написать игру "О, счастливчик!". На экране по очереди появляются вопросы и варианты ответов. Неправильный выбор - игра окончена. Правильный ответ - переходим к следующему вопросу. Если все ответы правильные - в конце выводится сообщение о победе. По желанию можно реализовать несгораемые суммы, подсказки, работу с файлами, звуковые эффекты и тд')
        print("")
        print("Начинаем!")

        file = open('quiz.txt',mode='r',encoding='utf-8')
        content_quiz = file.read()
        file.close()

        answer=''#ответ
        record=0#баллы
        l_quiz1 = ''#первая строка: подводка к вопросу
        l_quiz2 = ''#вторая строка: вопрос
        l_quiz3 = ''#третья строка: подсказка
        l_quiz4 = ''#четвертая строка: ответ
        l_quiz5 = ''#пятая строка: баллы

        l_quiz_all = list()
        l_quiz_all = content_quiz.split('\n')
#        print("l_quiz_all: ", l_quiz_all)
        q_num_all = len(l_quiz_all)
#        print("q_num_all = ", q_num_all)
        for i in range(0, q_num_all, 5):
            l_quiz1+=l_quiz_all[i]+'\n'
#            print("l_quiz1:\n", l_quiz, ", i: ", i)

        l_quiz1=l_quiz1.split('\n')
        l_quiz1.remove('')

        for i in range(1, q_num_all, 5):
            l_quiz2+=l_quiz_all[i]+'\n'
            i+=5
        l_quiz2=l_quiz2.split('\n')
        l_quiz2.remove('')

        for i in range(2, q_num_all, 5):
            l_quiz3+=l_quiz_all[i]+'\n'
            i+=5
        l_quiz3=l_quiz3.split('\n')
        l_quiz3.remove('')

        for i in range(3, q_num_all, 5):
            l_quiz4+=l_quiz_all[i]+'\n'
            i+=5
        l_quiz4=l_quiz4.split('\n')
        l_quiz4.remove('')

        for i in range(4, q_num_all, 5):
            l_quiz5+=l_quiz_all[i]+'\n'
            i+=5
        l_quiz5=l_quiz5.split('\n')
        l_quiz5.remove('')

        for i in range(len(l_quiz1)):
            print(l_quiz1[i], l_quiz2[i], sep='\n')
            answer = input("Ваш ответ: ")
            if answer=='подсказка':
                print(l_quiz3[i])
                if l_quiz3[i]=='сейчас откроется ссылка':
                    print("Чтобы продолжить, закройте браузер")
                    K()
                elif l_quiz3[i]=='ВЗДРЫЖЪНИ ЭФФЕКТ':
                    U()
                answer = input("Ваш ответ: ")
                if answer == l_quiz4[i]:
                    print("Вы правы!")
                    record+=int(l_quiz5[i])/2
                else:
                    print("Вы ошиблись")
                    break
            elif answer == l_quiz4[i]:
                print("Вы правы!")
                record+=int(l_quiz5[i])
            else:
                print("Вы ошиблись")
                break
        if record==50*len(l_quiz1):
            print("Поздравляю! Вы победили!")
            print("Вы набрали ", record, "баллов")
        else:
            print("Вы набрали ", record, "баллов")


    cont=input("Повторить выбор задачи? y\n")
