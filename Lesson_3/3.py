#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.


from random import random, randint

N = 10
numbers = [0] * N

for i in range(N):
    val = randint(0, 100)
    numbers[i] = val
print(numbers)

min_idx = 0
max_idx = 0
min_num = numbers[min_idx]
max_num = numbers[max_idx]

for i in range(1, N):
    if numbers[i] < min_num:
        min_num = numbers[i]
        min_idx = i
    elif numbers[i] > max_num:
        max_num = numbers[i]
        max_idx = i
numbers[min_idx], numbers[max_idx] = max_num, min_num
print(numbers)


