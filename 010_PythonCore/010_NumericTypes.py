#  Числа - неизменяемые объекты!

# Эти формы записи эквивалентны:
# from decimal import Decimal as ddd, затем a = ddd(123)
# import decimal, затем a = decimal.Decimal(123)

import decimal
import fractions
import sys


# сравнение float в пределах машинной точности
def equal_float(_a, _b):
    return abs(_a - _b) <= sys.float_info.epsilon


# bool - числовой тип, True = 1, False = 0
b1 = True
b2 = False
b3 = bool(5)
print(b1 + b2 + b1 + b3)

# Способы задания чисел
a = 10
b = int(10)
c = 0b1010  # bin
d = int(0o12)  # oct
e = 0xA  # hex
f = int('0xFF', 16)  # из строки

print(10 // 3, 10 % 3, 10 ** 2, round(10 / 3, 2))
print(divmod(10, 3))  # деление с остатком, результат в виде кортежа

print(bin(a), hex(a), oct(a))  # строковое представление

# Битовые операции
i = 0b1111_1111
j = 0b0000_1111
print('i = {0:b} ~i = {1:b}'.format(i, ~i))  # ???
print('{0:b} & {1:b} = {2:b}'.format(i, j, i & j))
print('{0:b} | {1:b} = {2:b}'.format(i, j, i | j))
print('{0:b} ^ {1:b} = {2:b}'.format(i, j, i ^ j))
print('{0:b} >> 1 = {1:b}'.format(i, i >> 1))
print('{0:b} << 2 = {1:b}'.format(i, i << 2))

fl = float(8.9e-4)  # float, не подходят для фин. вычислений
print(sys.float_info)  # инфо по float: мин макс погрешность и т.д.

c1 = 1 + 1j  # complex, j - мнимая часть
c2 = complex(0, 1)  # комплексная единица
print(c1.real, c1.imag, c2 ** 2)

print(decimal.Decimal(1 / 3))  # гарантированная точность, подходят для фин.вычислений

r = fractions.Fraction(1, 3)  # рациональные числа(дроби вида 1/3)
print(r, r + r, r * r, r ** r)

