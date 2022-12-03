# Дескриптор доступа
# в основе дескриптора("контроллера доступа") лежат спец.методы
# доступа к атрибутам __get__, __set__, __delete__

class MyDecorator:

    def __init__(self, funcget=None, funcset=None):
        self.funcget = funcget
        self.funcset = funcset

    # спец.методы, отрабатываю при чтении/установке свойства через точку: а.х
    def __get__(self, obj, objtype=None):
        value = self.funcget(obj)
        print('__get__:', value)
        return value

    def __set__(self, obj, value):
        print('__set__:', value)
        self.funcset(obj, value)

    # установщик функции-геттера, возвращается новый объект-декоратор,
    # в котором функция-геттер инициализирукется переданным значением,
    # а функция-сеттер копируется из объекта-источника
    def set_getter(self, funcget):
        type_ = type(self)  # = MyDecorator
        return type_(funcget, self.funcset)

    def set_setter(self, funcset):
        type_ = type(self)  # = MyDecorator
        return type_(self.funcget, funcset)


class A:

    def __init__(self, x):
        self.__x = x

    # Варианты синтаксиса:
    #
    # 1. @MyDecorator - в таком варианте при создании декоратора в __init__
    # декоратора первым параметром сразу прилетает функция x()
    # @MyDecorator() <=> x =  MyDecorator(x)
    #
    # 2. @MyDecorator().set_getter <=> x = MyDecorator().set_getter(x)
    # cначала создается экземпляр декоратора (funcget не инициализирован),
    # а затем для него вызывается установщик функции-геттера,  которому и
    # передается x()
    @MyDecorator  # создание объекта-декоратора через __init__(funcget = x)
    def x(self):
        print('')

    # @x.set_setter <=> x = x.set_setter(x)
    # Эквивалент, тут сложнее т.к. нужно предварительно сохранить геттер,
    # перед тем как затереть х, а затем пересоздать декоратор с
    # геттером/сеттером:
    # f = x.funcget
    # def x(self, value):
    #    self.__x = value
    # x = MyDecorator(f, x)
    @x.set_setter  # x уже указывает на объект декоратора!
    def x(self, value):
        self.__x = value


a = A(5)

a.x = 10
