# вычисляемый атрибут с помощью дескриптора
# size - это атрибут и он имеет тип DirectorySize, каждый раз
# когда выполняется d.size, фактически создается новый объект DirectorySize()
# а для него уже вызывается ЕГО метод __get__(...)

import os


class DirectorySize:

    def __get__(self, instance, owner):
        return len(os.listdir(instance.dirname))


class Directory:

    def __init__(self, dirname):
        self.dirname = dirname

    size = DirectorySize()


d = Directory('.')
print(d.size)
