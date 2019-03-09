"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def with_series(n):
    count = 0
    for i in range(len(n)):
        div = str(1) + '0' * i
        div_shift = div + '0'
        if int(div) == 1:
            if (int(n) % 10) % 2 == 0:
                count += 1
        elif i + 1 == len(n):
            if (int(n) // int(div)) % 2 == 0:
                count += 1
        else:
            if ((int(n) % int(div_shift)) // int(div)) % 2 == 0:
                count += 1
    print('Четных цифр в числе:', count)
    print('Нечетных цифр в числе:', len(n) - count)


def with_recursion(n, m, count=0):
    if m == 1:
        if (n % 10) % 2 == 0:
            count += 1
        print('Четных цифр в числе:', count)
        print('Нечетных цифр в числе:', len(str(n)) - count)
    elif len(str(m)) == len(str(n)):
        number = n // m
        if number % 2 == 0:
            count += 1
        return with_recursion(n, int(m / 10), count)
    else:
        number = (n % (m * 10)) // m
        if number % 2 == 0:
            count += 1
        return with_recursion(n, int(m / 10), count)


def with_array(n):
    count = 0
    for num in n:
        if int(num) % 2 == 0:
            count += 1
    print('Четных цифр в числе:', count)
    print('Нечетных цифр в числе:', len(n) - count)


number = input('Введите натуральное число:')
print(number)
divider = str(1) + '0' * (len(number) - 1)
print('Решение через рекурсию:')
with_recursion(int(number), int(divider))
print('\nРешение через цикл:')
with_series(number)
print('\nРешение через цикл + массив:')
with_array(number)


