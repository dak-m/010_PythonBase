# Реализация итерируемого объекта с помощью __getitem__

class MyIterable2(object):
    def __init__(self):
        self.items = [1, 2, 3, 4]

    def __getitem__(self, item):
        if len(self.items) > item:
            return self.items[item]
        else:
            raise IndexError


obj = MyIterable2()  # итерируемый объект
iterat = iter(obj)  # итератор

print(next(iterat))
print(next(iterat))
print(next(iterat))
