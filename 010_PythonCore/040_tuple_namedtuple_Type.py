# кортежи являются НЕИЗМЕНЯЕМЫМИ, относятся к ПОСЛЕДОВАТЕЛЬНОСТЯМ (т.е упорядочены)

import math
# именованные кортежи
from collections import namedtuple

# распаковка кортежа в переменые
MANUFACTURER, MODEL, SEATING = (0, 1, 2)
MINIMUM, MAXIMUM = (0, 1)
aircraft = ("Airbus", "A320-200", (100, 220))
print(aircraft[SEATING][MAXIMUM])

for x, y in ((-3, 4), (5, 12), (28, -45)):
    print(math.hypot(x, y))

for z in ((-3, 4), (5, 12), (28, -45)):
    x, y = z
    print(math.hypot(x, y))
    print(math.hypot(*z))


# именованные кортежи
Sale = namedtuple('Sale', 'product price')
adsale = Sale('adidas', 200)
print('{0} {1}'.format(*adsale))
print('{0.product} {0.price}'.format(adsale))

Aircraft = namedtuple('Aircraft', 'model, seating')
Seating = namedtuple('Seating', 'minimum maximum')
aircraft = Aircraft('BOING', Seating(100, 200))


# фичи с распаковкой

a = 1
b = 2
# классика питона
b, a = (a, b)

c = (1, 2, 3, 4, 5)
# перегнать кортеж в список
*d, = c

e, *_ = c  # голова, если остальное не нужно
*_, f = c  # хвост, если остальное не нужно
g, *_, h = c  # и т.д., переменную перед которой стоит * следует понимать как "список, содержащий все остальное"
print(_)  # '_' обычно применяется для игнорирования того что не нужно

# генератор кортежа, по аналогии со списками
t = tuple(range(10))
u = tuple((n, n**2) for n in range(10))  # в отличие от списка, просто u = (n**2 for n in range(10)) не прокатит
