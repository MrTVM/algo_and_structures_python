"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

class My_hex:
    def __init__(self, x):
        self.x = list(x)
        self._hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,\
                            '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,\
                            'C': 12, 'D': 13, 'E': 14, 'F': 15}
        self._hex_keys = list(self._hex_dict.keys())
        self._hex_val = list(self._hex_dict.values())

    def __add__(self, obj):
        self.sum = []
        self.x = list(reversed(self.x))
        obj.x = list(reversed(obj.x))

        count_element = len(self.x) - len(obj.x)
        if count_element > 0:
            obj.x.append('0' * count_element)
            count_element = len(self.x)
        else:
            self.x.append('0' * (count_element * -1))
            count_element = len(obj.x)

        memory = 0
        for i in range(count_element):
            sum = self._hex_dict.get(self.x[i]) + self._hex_dict.get(obj.x[i]) + memory
            if sum >= 16:
                val = self._hex_keys[self._hex_val.index(sum - 16)]
                self.sum.append(val)
                memory = 1
            else:
                val = self._hex_keys[self._hex_val.index(sum)]
                self.sum.append(val)
                memory = 0
        self.sum = list(reversed(self.sum))


a = input('Введите число:').upper()
b = input('Введите число:').upper()
a = My_hex(a)
b = My_hex(b)
a + b
print(a.sum)





