"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return sum_numbers(n - 1) + n


def formula(n):
    return (n * (n + 1)) / 2


# n = int(input('Введите верхнюю границу множества:'))
n = 10
for i in range(1, n + 1):
    if sum_numbers(i) != formula(i):
        print('Утверждение неверно для n = ', i)
if i == n:
    print('Для множеств до n = {} утверждение верно!'.format(i))

