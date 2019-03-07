# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

a = bin(5)
b = bin(6)
print('Битовые записи: 5 = {} и 6 = {}'.format(a, b))


bit_and = int(a, 2) & int(b, 2)
bit_or = int(a, 2) | int(b, 2)
bit_xor = int(a, 2) ^ int(b, 2)
bit_not = ~ int(a, 2)


print('Результат операции "AND": {} = {}'.format(bin(bit_and), bit_and))
print('Результат операции "OR": {} = {}'.format(bin(bit_or), bit_or))
print('Результат операции "XOR": {} = {}'.format(bin(bit_xor), bit_xor))
print('Результат операции "NOT": {} = {}'.format(bin(bit_not), bit_not))


left_shift = int(a, 2) << 2
right_shift = int(a, 2) >> 2


print('Сдвиг влево на 2 знака: {} = {}'.format(bin(left_shift), left_shift))
print('Сдвиг вправо на 2 знака: {} = {}'.format(bin(right_shift), right_shift))

