# генератор - это функция "помнящая" свое состояние
# генератор возвращает итератор
# генератор более простая альтернатива определения класса итератора,
# т.к. класс итератора создавать не нужно

# способ создания генератора 1:
def fibonacci(xterms):
    # первые два условия
    x1 = 0
    x2 = 1
    count = 0

    if xterms <= 0:
        print("Укажите целое число больше 0")
    elif xterms == 1:
        print("Последовательность Фибоначчи до", xterms, ":")
        print(x1)
    else:
        while count < xterms:
            xth = x1 + x2
            x1 = x2
            x2 = xth
            count += 1
            yield xth


fib = fibonacci(5)
print(fib, type(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


# получение элементов из генератора с помощью прямого вызова next()
def generator_list_items(collection):
    for item in collection:
        yield item


gen = generator_list_items(['Python', 'Java', 'C', 'C++', 'CSharp'])
while True:
    try:
        print(next(gen))
    except StopIteration:
        break


