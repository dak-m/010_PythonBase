# @staticmethod встроенный "дескриптор без данных", реализованный на С(как и
# всё остальное из buildins.py) Примечание: модуль buildins.py "не
# настоящий", его "восстановил" PyCharm, но там только заглушки-сигнатуры
# функций, поэтому отладчик конечно туда не зайдет...
# Дескриптор по сути является декоратором, контролирующим доступ к атрибуту
# Реализация staticmethod на Python выглядела бы как-то так:

class MyStaticMethod(object):
    """Emulate PyStaticMethod_Type() in Objects/funcobject.c"""

    def __init__(self, f):
        print(f'__init__: {self}')
        self.f = f

    def __get__(self, obj, objtype=None):
        print(f'__get__: {self}')
        return self.f

    # зачем объект этого класса делать вызываемым??? Оказывается для вызова с
    # помощью __dict__: Person.__dict__['hellow_2']()
    def __call__(self, *args, **kwds):
        print(f'__call__: {self}')
        return self.f(*args, **kwds)


def print_hellow():
    print('Hellow_3')


class Person:

    def hellow_0(self):
        print('Hellow_0')

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

# Удивительно! Но они различаются:
print(Person.hellow_2)
print(Person.__dict__['hellow_2'])  # <=> vars(Person)['hellow_2']

print('*'*80)
Person.hellow_2()  # вызов через __get__
Person.__dict__['hellow_2']()  # вызов через __call__
