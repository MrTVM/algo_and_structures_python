"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random

min_number_range = int(input('Введите число (нижнюю границу диапазона):'))
max_number_range = int(input('Введите число (верхнюю границу диапазона):'))

number_random_int = random.randint(min_number_range, max_number_range + 1)
print('Случайное целое число: {}'.format(number_random_int))


min_number_range = int(input('Введите число (нижнюю границу диапазона):'))
max_number_range = int(input('Введите число (верхнюю границу диапазона):'))

number_random_uni = random.uniform(min_number_range, max_number_range + 1)
print('Случайное вещественное число: {}'.format(number_random_uni))

first_letter = str(input('Введите с какой буквы начать:')).lower()
last_letter = str(input('Введите какой буквой закончить:')).lower()

number_letter_int = random.randint(ord(first_letter), ord(last_letter) + 1)
print('Случайный символ: {}'.format(chr(number_letter_int)))

