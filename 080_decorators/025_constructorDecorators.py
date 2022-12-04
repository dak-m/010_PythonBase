# конструктор декораторов
def bounded(minimum, maximum):
    def decorator(function):
        # minimum, maximum находятся в области видимости enclosing scope
        # т.е. объемлющей(внешней) функции для функции decorator и при этом 
        # используются в самой decorator и поэтому они попали к ней в замыкание
        def wrapper(*args, **kwargs):
            # тут кроме minimum, maximum в замыкание попадает ещё и наша
            # function
            result = function(*args, **kwargs)
            if result > maximum:
                return maximum
            elif result < minimum:
                return minimum
            return result
        return wrapper
    return decorator


decorator_1 = bounded(1, 100)
decorator_2 = bounded(10, 1000)

# значения переменных, попавших в замыкание
print([c.cell_contents for c in decorator_1.__closure__])
print([c.cell_contents for c in decorator_2.__closure__])


# boundet(20, 30) возвращает декоратор с уже установленными параметрами,
# которым затем и декорируется функция, т.е. сначала decor = boundet(20, 30),
# затем func_1 = decor(func1)
@bounded(20, 30)
def func_1(x):
    return x


# в замыкании у функции wrapper находится декорируемая функция
# и значения параметров minimum, maximum
# цепочка ссылок: funс_1 --> wrapper --> старая_func_1, minimum, maximum
print([c.cell_contents for c in func_1.__closure__])
print(func_1(15), func_1(25), func_1(35))

# можно поменять значение переменной в замыкании
func_1.__closure__[1].cell_contents = 100
print(func_1(15), func_1(25), func_1(35))
