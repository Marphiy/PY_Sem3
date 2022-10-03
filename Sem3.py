from operator import ne
import os
import time
import random
import math
from random import randint


def random_int_fill_list(size, limfrom, limto):
    new_list = []
    for i in range(size):
        new_list.append(randint(limfrom, limto))
    return new_list


def random_float_fill_list(size):
    new_list = []
    for i in range(size):
        new_list.append(round(random.random() * 10, 2))
    return new_list

def check_for_enter_error():
    while True:
        numb = input('Введите любое целое положительное число больше 0: ')
        if numb.isdigit():
            numb = int(numb)
            if numb == 0:
                os.system('cls' if os == 'nt' else 'clear')
                print('Число должно быть больше 0! Повторите ввод!')
            else: break
        else: 
            os.system('cls' if os == 'nt' else 'clear')
            print('Ошибка ввода!') 
    return int(numb)

def fib(n):
    if n in [1, 2]:
        return 1
    elif n == -1:
        return 1
    elif n == -2:
        return -1
    elif n > 0:
        return fib(n - 1) + fib(n - 2)
    elif n < -2:
        return fib(n + 1) + fib(n + 2)
    elif n == 0:
        return 0

def zadacha_19():  # 19. Реализуйте алгоритм задания случайных чисел без использования
    # встроенного генератора псевдослучайных чисел.
    os.system('sls' if os == 'nt' else 'clear')
    # n = 10
    # a = 1234
    # c = 89567
    # m = 45
    # my_list = []
    # for i in range(n):
    #     my_list.append(round(((a ** i - 1) / (a - 1) * c) % m))
    # print(my_list)

    # my_list = ([int(str(time.time())[-1]) for i in range(10)])
    # print(my_list)

    seconds = time.time()
    rand = int(100*(seconds % 1))
    print(rand)


def zadacha_20():  # 20. Задайте список. Напишите программу, которая определит,
    # присутствует ли в заданном списке строк некое число.
    os.system('sls' if os == 'nt' else 'clear')
    string_1 = ['sdf34sdf', 'lkj324o', 'poics99l', '93n1', 'mklja56a8']
    print(string_1)
    numb = int(input('Введите искомое число: '))
    count = 0
    for i in string_1:
        # if i.find(str(numb)) != -1:
        #     print(f'{i} содержит {numb}')
        if str(numb) in i:
            print(f'{i} содержит {numb}')
            count += 1
    if count == 0:
        print(f'{numb} не содержится в списке')


def zadacha_21():  # 21. Напишите программу, которая определит позицию второго вхождения
    # строки в списке либо сообщит, что её нет.
    os.system('sls' if os == 'nt' else 'clear')
    list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    my_str = input('Введите строку: ')
    count = 0
    v_index = 0
    for i in range(len(list_1)):
        if my_str == list_1[i]:
            count += 1
        if count == 2:
            v_index = i
            break
    if count == 0:
        print(f'У {my_str} нет вхождения в {list_1}')
    elif count < 2:
        print(f'У {my_str} нет второго вхождения в {list_1}')
    elif count == 2:
        print(f'У {my_str} имеется второе вхождения в {list_1} с индексом {v_index}')


def zadacha_22():   # 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт
    # сумму элементов списка, стоящих на нечётной позиции.
    os.system('sls' if os == 'nt' else 'clear')
    size = 10
    rand_from = -44
    rand_to = 44
    my_list = random_int_fill_list(size, rand_from, rand_to)
    sum_of_odd_ind_elms = 0
    for i in range(1, len(my_list), 2):
        sum_of_odd_ind_elms += my_list[i]
    print(
        f'Сумма элементов списка {my_list} с нечетными индексами = {sum_of_odd_ind_elms}')


def zadacha_23():   # 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой
    # считаем первый и последний элемент, второй и предпоследний и т.д.
    os.system('sls' if os == 'nt' else 'clear')
    size = int(input('Введите количество элементов списка: '))
    rand_from = 0
    rand_to = 20
    my_list = random_int_fill_list(size, rand_from, rand_to)
    pairs_mult = 1
    res = []
    for i in range(math.ceil(size / 2)):
        pairs_mult = my_list[i] * my_list[size - 1 - i]
        res.append(pairs_mult)
    print(
        f'Произведения пар элементов списка {my_list} "снаружи внутрь" = {res}')
    print()


def zadacha_24():  # 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт
    # разницу между максимальным и минимальным значением дробной части элементов.
    os.system('cls' if os == 'nt' else 'clear')
    size = 10
    my_list = random_float_fill_list(size)
    print(my_list)
    new_lst = ([round(i % 1, 2) for i in my_list])
    print(new_lst)
    res = max(new_lst) - min(new_lst)
    print(res)
    # ИЛИ:
    # print(my_list)
    # min_val = 99
    # max_val = 0
    # for i in range(size):
    #     if my_list[i] % 1 < min_val and my_list[i] % 1 != 0:
    #         min_val = round(my_list[i] % 1, 2)
    #     elif my_list[i] % 1 > max_val:
    #         max_val = round(my_list[i] % 1, 2)
    
    # print(f'Максимальное значение дробной части элементов списка: {max_val}')
    # print(f'Минимальное значение дробной части элементов списка: {min_val}')
    # print(f'Разница между максимальным и минимальным значением дробной части элементов составляет {round(max_val -  min_val, 2)}')

def zadacha_25():   #25. Напишите программу, которая будет преобразовывать 
    # десятичное число в двоичное.
    os.system('cls' if os == 'nt' else 'clear')
    sys_sch = 2
    numb = check_for_enter_error()
    # while True:
    #     numb = input('Введите любое целое положительное число больше 0: ')
    #     if numb.isdigit():
    #         numb = int(numb)
    #         if numb == 0:
    #             os.system('cls' if os == 'nt' else 'clear')
    #             print('Число должно быть больше 0! Повторите ввод!')
    #         else: break
    #     else: 
    #         os.system('cls' if os == 'nt' else 'clear')
    #         print('Ошибка ввода!')  
    os.system('cls' if os == 'nt' else 'clear')
    numb_res = numb
    my_list = []
    while int(numb_res) > 0:
        my_list.insert(0, int(numb_res % sys_sch))
        numb_res /= sys_sch
    my_str: str = ""
    for i in my_list:
        my_str += str(i)
    my_str = int(my_str)
    print(f'{numb} в {sys_sch}-й системе счисления: {my_str}')
    
def zadacha_26():   # 26. Задайте число. Составьте список чисел Фибоначчи, 
    # в том числе для отрицательных индексов.
    os.system('cls' if os == 'nt' else 'clear')
    numb = check_for_enter_error()
    my_list = []
    for i in range(-numb, numb + 1):
        my_list.append(fib(i))
    print(my_list)
    

        
   
    

# zadacha_19()
# zadacha_20()
# zadacha_21()
# zadacha_22()
# zadacha_23()
zadacha_24()
# zadacha_25()
# zadacha_26()