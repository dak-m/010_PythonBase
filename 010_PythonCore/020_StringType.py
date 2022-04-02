# Строки - неизменяемый тип!

from unicodedata import normalize

str1 = "Hello world!!!".title()         # судя по всему строка - это объект ))
str2 = '\nHello world!!!    '.rstrip()  # удаление пробелов справа
str3 = '''"Hello 'w'orld!!!'''          # тройные одинарные(двойные) кавычки - сила!
str4 = '\tHello \'world!!!'             # экранирование куда ж без него?

# многострочный текст
str5 = '''123
456\
789'''

# хороший способ задать многострочный текст
str6 = ("123"
        "456"
        "789")

# сырая строка, все символы интерпретируются как обычные, нет необходимости экранировать
str7 = r'////\\\\'


# Юникод
euros = "€ \N{euro sign} \u20AC \U000020AC"    # \u 16бит юникод, \U 32бит юникод
print(euros)
print(ord(euros[0]), hex(ord(euros[0])))  # получение юникод-кода символа из строки

str8 = "anarchists are " + chr(8364) + chr(0x20ac)  # получение строки из юникод-кода
print(str8)
print(ascii(str8))  # получение строки в ascii, не ascii-символы будут заменены на упр.послед.юникода вида \u...

a = ascii('②⓪⑦④⑨').strip('\'\"')
b = bytes(a, 'ascii').decode('unicode-escape')
print(a, b)

# При сравнении строк в юникод, есть проблема:
# один и тот же символ может быть задан несколькими способами, решение проблемы - нормализаия

a0 = '\u00C5'
# символ Å с юникодом \u00C5 может быть закодирован 3-мя способами:
a1 = b'\xE2\x84\xAB'.decode()
a2 = b'\xC3\x85'.decode()
a3 = b'\x41\xCC\x8A'.decode()

print(a0, a1, a2, a3)
print(a0 == a1, a0 == a2, a0 == a3)
print(normalize('NFKD', a0) == normalize('NFKD', a1),
      normalize('NFKD', a0) == normalize('NFKD', a2),
      normalize('NFKD', a0) == normalize('NFKD', a3))

# 'умножение'  строки
print(str1*2)

treatises = ["123", "456", "789"]
print(" ".join(treatises))

# разбор строк вида ключ=значение
s = 'param=value'
print(s.partition('='))

# определение типа файла по расширению
filename = 'picture.jpg'
if filename.lower().endswith(('.jpg', '.jpeg')):
    print(filename, 'is JPEG')
