"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""


from random import random, randint

N = 10
numbers = [0] * N

for i in range(N):
    val = randint(1, 10)
    numbers[i] = val
print(numbers)


first_min_num = numbers[0]
second_min_num = numbers[0]

for number in numbers:
    for num in numbers:
        if number < first_min_num:
            first_min_num = number
        if numbers.count(first_min_num) >= 2:
            second_min_num = first_min_num
        elif first_min_num < number < second_min_num:
            second_min_num = number
print(first_min_num, second_min_num)



