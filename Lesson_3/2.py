"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import random, randint

N = 10
numbers = [0] * N

for i in range(N):
    val = randint(0, 100)
    numbers[i] = val
print(numbers)

even_num = []
count = 1
for number in numbers:
    if number % 2 == 0:
        even_num.append(count)
    count += 1
print(even_num)


