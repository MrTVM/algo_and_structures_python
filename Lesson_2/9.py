"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

def sum_with_recursion(n, m, result=0):
    if m == 1:
        result = n % 10 + result
        return result
    elif len(str(m)) == len(str(n)):
        number = n // m
        result = number + result
        return sum_with_recursion(n, int(m / 10), result)
    else:
        number = (n % (m * 10)) // m
        result = number + result
        return sum_with_recursion(n, int(m / 10), result)


def sum_with_series(number):
    for i in range(len(number)):
        div = str(1) + '0' * i
        div_shift = div + '0'
        if int(div) == 1:
            num = int(number) % 10
            result = num
        elif i + 1 == len(number):
            num = int(number) // int(div)
            result = result + num
        else:
            num = (int(number) % int(div_shift)) // int(div)
            result = result + num
    return result


num1 = input('Введите число 1:')
num2 = input('Введите число 2:')

divider = str(1) + '0' * (len(num1) - 1)
sum1 = sum_with_recursion(int(num1), int(divider))
sum2 = sum_with_series(num2)

if sum1 > sum2:
    print('Сумма цифр числа {} = {}'.format(num1, sum1))
else:
    print('Сумма цифр числа {} = {}'.format(num2, sum2))

