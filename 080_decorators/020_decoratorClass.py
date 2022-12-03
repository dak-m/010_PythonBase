# класс декоратор, при декорировании функции происходит test = MyDecorator(test)
# при вызове объекта класс MyDecorator(..) вызывается спец.метод __call__
class MyDecorator:
    
    def __init__(self, func):
        self.__func = func
        
    def __call__(self, *args, **kwargs):
        print('decorator: ', end='')
        return self.__func(*args, **kwargs)

    # Можно при необходимости переопределить спец.метод на свой:
    # def mycall(self, *args, **kwargs):
    #     print('mycall decorator: ', end='')
    #     return self.__func(*args, **kwargs)
    # __call__ = mycall
    
    
def test(p):
    print(p)


test('Arg')
test = MyDecorator(test)  # <=> @MyDecorator
test('Arg')
