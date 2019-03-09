"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

def with_recrusion(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return with_recrusion(n - 1) + 1 / 2**n
    else:
        return with_recrusion(n - 1) - 1 / 2**n


def with_series(n):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            result = 1 / 2**i + result
        else:
            result = -1 / 2**i + result
    return result

n = int(input('Введите длину ряда:'))
print(with_series(n))
print(with_recrusion(n - 1))

