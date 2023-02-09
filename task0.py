# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

list_num1 = []
for i in range(int(input('Введите размер первого набора чисел -> '))):
    list_num1.append(random.randint(1, 10))

list_num2 = []
for i in range(int(input('Введите размер второго набора чисел -> '))):
    list_num2.append(random.randint(1, 10))

print(*list_num1)
print(*list_num2)

set_num1 = set(list_num1)
set_num2 = set(list_num2)

set_result = set_num1.intersection(set_num2)
print(*sorted(set_result))
