# @staticmethod встроенный "дескриптор без данных", реализованный на С(как и
# всё остальное из buildins.py) Примечание: модуль buildins.py "не
# настоящий", его "восстановил" PyCharm, но там только заглушки-сигнатуры
# функций, поэтому отладчик конечно туда не зайдет...
# Дескриптор по сути является декоратором, контролирующим доступ к атрибуту
# Реализация staticmethod на Python выглядела бы как-то так:

class MyStaticMethod(object):
    """Emulate PyStaticMethod_Type() in Objects/funcobject.c"""

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f


def print_hellow():
    print('Hellow_3')


class Person:

    # стандартное объявление статичного метода
    @staticmethod
    def hellow_1():
        print('Hellow_1')

    # Моя эмуляция @staticmethod
    @MyStaticMethod
    def hellow_2():
        print('Hellow_2')

    # Но в статичный метод можно превратить любую функцию, даже не
    # принадлежащую классу
    hellow_3 = staticmethod(print_hellow)


Person.hellow_1()
Person.hellow_2()
Person.hellow_3()
