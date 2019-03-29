"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random

def search_med_value(arr):
    for i in range(len(arr)):
        left_count = 0
        for j in range(len(arr)):
            if arr[i] >= arr[j]:
                left_count += 1
        if left_count == len(arr) // 2 + 1:
            break
    return arr[i]


m = 5
my_arr = [random.randint(1, 100) for _ in range(2 * m + 1)]
print(my_arr)
print('Медиана: ', search_med_value(my_arr))
print('Проверка медиана = ', sorted(my_arr)[m])





