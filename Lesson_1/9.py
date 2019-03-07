# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
num3 = int(input('Введите третье число:'))

avg_num = num1

if num1 < num2 < num3:
    avg_num = num2
elif num1 < num3 < num2:
    avg_num = num3

print('Среднее число', avg_num)

