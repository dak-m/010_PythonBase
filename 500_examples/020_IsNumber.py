# проверка числа

import string


def isnumber1(data_):
    isnumber = True
    numbers = [str(s) for s in range(10)]
    for s in data_:
        if s not in numbers:
            isnumber = False
            break
    return isnumber


def isnumber2(data_):
    return not (frozenset(data_) - frozenset(string.digits))


data = input('input number: ')
print(isnumber1(data))
print(isnumber2(data))
print(data.isdigit())  # так конечно проще)))
