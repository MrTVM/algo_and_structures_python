#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

first_letter = input('Введите первую букву:').lower()
second_letter = input('Введите вторую букву').lower()

start_number_in_alphabet = ord('a')
pos_first_letter = ord(first_letter) - start_number_in_alphabet + 1
pos_second_letter = ord(second_letter) - start_number_in_alphabet + 1
distance = pos_second_letter - pos_first_letter

print('Позиция буквы {} в алфавите: {}'.format(first_letter, pos_first_letter))
print('Позиция буквы {} в алфавите: {}'.format(second_letter, pos_second_letter))
if distance > 0:
    print('Между буквами {} симв.'.format(distance))
else:
    print('Между буквами {} симв.'.format(distance*-1))


