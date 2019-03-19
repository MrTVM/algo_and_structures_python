"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
import cProfile


# первый алгоритм
def simple_num1(n=300):
    lst = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst

# Решето Эратосфена
def simple_num2(n=300):
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return lst


# Оценка на время выполнения алгоритма
print(timeit.timeit('simple_num1()', setup="from __main__ import simple_num1", number=1000))
print(timeit.timeit('simple_num2()', setup="from __main__ import simple_num2", number=1000))

def main():
    n = 500
    simple_num1(n)
    simple_num2(n)

cProfile.run('main()')

"""
По простой оценке на валовое исполнение алгоритма по времени очевидно что
алгоритм Эратосфена бысрее сторит ряд простых чисел.

Скорее всего это связано с тем, что первый вариант реализации имеет сложность
O(n**2), так как там волженный цикл. n элементов может проверяется почти n раз.
А решето имеет линейную сложность.
"""


