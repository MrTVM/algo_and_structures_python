"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

def buuble_sort(arr, order=False):
    n = 1
    while n < len(arr):
        end_sorted = 0
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                end_sorted += 1
        if end_sorted == 0:
            break
        n += 1
    if order:
        arr = list(reversed(arr))
    print(n)
    return arr


my_arr = [random.randint(-100, 100) for _ in range(10)]
print(my_arr)
print(buuble_sort(my_arr))



