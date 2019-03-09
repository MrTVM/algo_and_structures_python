"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

def change_with_recursion(n, m, result=''):
    if m == 1:
        result = str(n % 10) + result
        print("Обратное число введенному будет:", result)
    elif len(str(m)) == len(str(n)):
        number = n // m
        result = str(number) + result
        return change_with_recursion(n, int(m / 10), result)
    else:
        number = (n % (m * 10)) // m
        result = str(number) + result
        return change_with_recursion(n, int(m / 10), result)


def change_with_series(number):
    for i in range(len(number)):
        div = str(1) + '0' * i
        div_shift = div + '0'
        if int(div) == 1:
            num = int(number) % 10
            result = str(num)
        elif i + 1 == len(number):
            num = int(number) // int(div)
            result = result + str(num)
        else:
            num = (int(number) % int(div_shift)) // int(div)
            result = result + str(num)
    print("Обратное число введенному будет:", result)



num = input('Введите число')
divider = str(1) + '0' * (len(num) - 1)
change_with_recursion(int(num), int(divider))
change_with_series(num)

