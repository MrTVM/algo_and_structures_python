"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

# составляем список простых чисел из последовательности длинной n
n = int(input("n="))
lst = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            # если делитель найден, число не простое.
            break
    else:
        lst.append(i)
print(lst)

# ищем i-й элемент в списке простых чисел
user_num = int(input('Введите номер искомого элемента:'))
print(lst[user_num - 1])


# Решето Эратосфена
a = list(range(n + 1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
print(lst)
print(lst[user_num - 1])



