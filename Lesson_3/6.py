"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random, randint

N = 10
numbers = [0] * N

for i in range(N):
    val = randint(1, 100)
    numbers[i] = val
print(numbers)

max_idx = 0
min_idx = 0
max_num = numbers[max_idx]
min_num = numbers[min_idx]

for i in range(N):
    for j in range(N):
        if numbers[i] > max_num:
            max_num = numbers[i]
            max_idx = i
        if numbers[i] < min_num:
            min_num = numbers[i]
            min_idx = i
if min_idx < max_idx:
    result = sum(numbers[min_idx + 1:max_idx])
    print('Индексы:\nмин = {}\nмакс = {}'.format(min_idx, max_idx))
else:
    result = sum(numbers[max_idx + 1:min_idx])
    print('Индексы:\nмакс = {}\nмин = {}'.format(max_idx, min_idx))
print('Сумма -', result)








