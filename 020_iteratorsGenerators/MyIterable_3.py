# Чтобы можно было итерироваться по объекту, у него должен быть метод __iter__,
# который вернет объект-итератор. У объекта-итератора(!!!) должен быть метод __next__,
# который будет возвращать следующий элемент из объекта, по которому итерируемся, либо кидать ошибку StopIteration
# В данном случае объект сам по себе и является итератором,
# но в общем случае объект и итератор не обязаны быть одним и тем же объектом.
# Например, у списка list итератором является отдельный объект list_iterator, а не сам список

class MyListIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            element = self._collection[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration

class MyListCollection:
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return MyListIterator(self._collection)


mycollection = [1, 2, 3]
aggregate = MyListCollection(mycollection)

for item in aggregate:
    print(item)

print("*" * 50)

itr = iter(aggregate)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break
