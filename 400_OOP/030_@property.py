class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _name):
        self.__name = _name


p = Person('Dima')
print(p.name)
p.name = 'Julia'
print(p.name)
