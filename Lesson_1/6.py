# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


letter_number = int(input('Введите номер буквы в алфавите (от 1 до 26):'))

number_first_letter_in_alphabet = ord('a')
pos_letter_number = number_first_letter_in_alphabet + letter_number - 1
letter = chr(pos_letter_number)

print('{} буква в алфавите - буква {}'.format(letter_number, letter))

