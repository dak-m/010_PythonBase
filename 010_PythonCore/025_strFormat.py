import datetime
import decimal
import locale
import math
import sys

print('{} {}'.format(1, 2))
print('{1} {0}'.format(1, 2))
print('{a} {b}'.format(a=1, b=2))

d = [1, 2]
print('{0[0]} {0[1]}'.format(d))
print('{} {}'.format(*d))

d = {'k1': 1, 'k2': 2}
print('{0[k1]} {0[k2]}'.format(d))
print('{k1} {k2}'.format(**d))  # <=> format(k1=d['k1'], k2=d['k2'])
print('{k1} {k2}'.format(k1=d['k1'], k2=d['k2']))

print('{0.pi} {1.maxunicode}'.format(math, sys))

# принудительно: s-строка, r-репрезентативная форма, a-репрезентативная форма ASCII
print('{0} {0!s} {0!r} {0!a}'.format(decimal.Decimal('93.4')))

s = "The sword of truth"
print("{0}".format(s))  # форматирование по умолчанию
print("{0:25}".format(s))  # минимальная ширина поля вывода 25
print("{0:>25}".format(s))  # выравнивание по правому краю, минимальная ширина 25
print("{0:^25}".format(s))  # выравнивание по центру, минимальная ширина 25
print("{0:-^25}".format(s))  # - заполнитель, по центру, минимальная ширина 25
print("{0:.<25}".format(s))  # . заполнитель, по левому краю, минимальная ширина 25
print("{0:.10}".format(s))  # максимальная ширина поля вывода 10

print("{0:{filler}<25}".format(s, filler='='))  # заполнитель во избежании путаницы лучше задавать так !!!


# динамическое определение формата
maxwidth = 25
print("{}".format(s[:maxwidth]))  # обычный срез
print("{0:=>{1}}".format(s, maxwidth))

# минимальная и максимальная ширина с заполнителем
print('{:{f}<{minw}.{maxw}}'.format('12345', minw=10, maxw=10, f='#'))
print('{:{f}<{minw}.{maxw}}'.format('1234567890qqqqq', minw=10, maxw=10, f='#'))

# числа

print('{0:0=12}'.format(12345))  # мин.ширина 12, 0 - символ заполнитель между знаком числа и значащими цифрами
print('{0:0=12}'.format(-12345))
# тоже самое другим способом
print('{0:012}'.format(12345))  # 012 - дополнить 0 до 12
print('{0:012}'.format(-12345))

# управление заполнением
print('{0:*<12}'.format(-12345))
print('{0:*>12}'.format(-12345))
print('{0:*^ 12}'.format(-12345))
print('{0:*^ 12}'.format(12345))

# вывод знака

print('{0:*^ 12}'.format(-12345))  # пробел или знак "-"
print('{0:*^ 12}'.format(12345))

print('{0:*^+12}'.format(-12345))  # знак всегда
print('{0:*^+12}'.format(12345))

print('{0:*^-12}'.format(-12345))  # "-" при необходимости (так работает по умолчанию)
print('{0:*^-12}'.format(12345))

# Вывод числа в разных системах исчисления
print("{0:b} {0:o} {0:x} {0:X} {0:d}".format(14613198))  # d - десятичная, по умолчанию
print("{0:#b} {0:#o} {0:#x} {0:#X} {0:#d}".format(14613198))

# n - вывод с учетом региональных настроек 
x, y = (1234567890.78, 1234.56)
locale.setlocale(locale.LC_ALL, "C")  # "С" - регион по умолчанию
c_ = "{0:n} {1:n}".format(x, y)  # с == "1234567890 1234.56"
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
en = "{0:n} {1:n}".format(x, y)  # en == "1,234,567,890 1,234.56"
# locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")
# de = "{0:n} {1:n}".format(x, y)  # de == "1.234.567.890 1.234,56"

# вещ.числа
# e-экспоненциальная форма, f-стандарт.форма
# g-общая форма, т.е. большие числа как e, маленькие как f
amount = (10 ** 3) * math.pi
print("[{0:12.2e}] [{0:12.2f}]".format(amount))
print("[{0:*>12.2e}] [{0:*>12.2f}]".format(amount))
print("[{0:*>+12.2e}] [{0:*>+12.2f}]".format(amount))
print('{0:.2%}'.format(0.5))  # точность 2, в процентах

# datetime форматирование
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# Комплексные числа
print("{0.real:.3f}{0.imag:+.3f}j".format(4.75917 + 1.2042j))
print("{0.real:.3f}{0.imag:+.3f}j".format(4.75917 - 1.2042j))
