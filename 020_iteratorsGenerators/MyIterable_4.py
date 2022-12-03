# функцию iter() можно вызывать с двумя аргументами,
# что позволит создать из вызываемого объекта(функция или класс с реализованным методом __call__) итератор.
# Первый аргумент должен быть вызываемым объектом, а второй — неким ограничителем.
# Вызываемый объект вызывается на каждой итерации и итерирование завершается,
# когда возбуждается исключение StopIteration или возвращается значения ограничителя.

class MyIterable4:
    def __init__(self):
        self.index = 0
        self.items = [1, 2, 3, 4]

    def __call__(self):
        value = self.items[self.index]
        self.index += 1
        return value


obj = MyIterable4()  # итерируемый объект
iterat = iter(obj, 3)  # итератор

print(next(iterat))  # 1
print(next(iterat))  # 2
print(next(iterat))  # StopIteration
