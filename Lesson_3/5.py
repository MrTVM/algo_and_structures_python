#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


from random import random, randint

N = 10
numbers = [0] * N

for i in range(N):
    val = randint(-10, 10)
    numbers[i] = val
print(numbers)

max_negative_num = 0
max_negative_idx = 0
for i in range(N):
    for j in range(N):
        if numbers[i] < max_negative_num and numbers[i] < 0:
            max_negative_num = numbers[i]
            max_negative_idx = i
if max_negative_num != 0:
    print('Макс. отриц. чило в массиве - {} с индеком {}'\
            .format(max_negative_num, max_negative_idx))
else:
    print('В массиве нет отрицательных значений')





