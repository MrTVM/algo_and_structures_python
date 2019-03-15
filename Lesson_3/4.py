# 4.	Определить, какое число в массиве встречается чаще всего.


from random import random, randint

N = 10
numbers = [0] * N

for i in range(N):
    val = randint(0, 5)
    numbers[i] = val
print(numbers)

max_count_num = numbers[0]
max_count = 0
for i in range(N):
    count = 0
    for j in range(N):
        if numbers[i] == numbers[j]:
            count += 1
    if count > max_count:
        max_count = count
        max_count_num = numbers[i]
print('Самое частое чило в массиве -', max_count_num)

# Можно через стандартную функцию count()
max_count_num = numbers[0]
max_count = numbers.count(max_count_num)

for num in numbers:
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        max_count_num = numbers[i]
print('Самое частое чило в массиве -', max_count_num)


