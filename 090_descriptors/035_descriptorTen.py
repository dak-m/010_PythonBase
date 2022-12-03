# Дескриптор - это объект, который переопределяет доступ к атрибуту другого
# объекта с помощью методов __get__(), __set()__, __delete()__ Эти три метода
# называются протоколом дескриптора. Если определен только метод __get__() то
# такой дескриптор называется "дескриптор без данных", если определены ещё и
# __set()__ или  __delete()__ или оба вместе, то это "дескриптор данных"
# @property, @staticmethod, @classmethod - это всё дескрипторы

class Ten:
    def __get__(self, instance, owner):
        return 10

    def __set__(self, instance, value):
        pass
        # raise AttributeError("can't set attribute")


class A:
    # Обычный атрибут класса, "прямой" доступ
    x = 5
    # Атрибут класса, досту к которому осуществляется с помощью дескриптора
    y = Ten()
    pass  # тут поставить точк останова, чтобы убедится, что y = __main__.Ten


a = A()
print(a.y)
#  Переменная y в словаре a.__dict__ отсутствует(т.к. это переменная класса
#  и находится в пространстве имен класса), но её создания не происходит!
#  вместо этого вызывается метод класса __set__. Если бы __set_ не был
#  определен, то создалась бы локальная переменная a.__dict__['y'] = 100,
#  таким образом дескриптор данных(т.е. у которого есть __set__) имеет
#  ПРИОРИТЕТ над локальным словарем __dict__
a.y = 100  # a.y по прежнему = 10!
print(a.y)