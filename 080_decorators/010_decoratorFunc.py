def decorator(func):
    print('decorator:', func)

    # функция-обертка, тут применено замыкание переменной func, которая
    # содержит декорируемую функцию
    def wrapper(*args, **kwargs):
        print(f'wrapper: func={func} args={args} kwargs={kwargs}')
        func(*args, **kwargs)

    return wrapper


# Это просто синтаксис!:
@decorator
def myfunc_a(*s, **d):
    print('myfunc_a:', s, d)


def myfunc_b(*s, **d):
    print('myfunc_b:', s, d)


# На самом деле происходит вот это:
myfunc_b = decorator(myfunc_b)

myfunc_a('1111', '2222', myvar='vars')
myfunc_b('1111', '2222', myvar='vars')

print(' ' * 80, '*' * 80, ' ' * 80, sep='\n')


# "Генератор декораторов" т.е. функция, возвращающая декоратор
def decorator_maker(mode=1):
    if mode == 1:
        return decorator
    else:
        # Создание нового декоратора. Вот что значит динамический язык!
        # Можно запросто на ходу вот так создавать функции:
        def decorator_b(func):
            # mode доступна внутри декоратора!!!
            print(f'decorator_b mode={mode} func={func}')

            def wrapper_b(*args, **kwargs):
                # mode доступна также внутри обертки!!!
                print(f'wrapper_b mode={mode} args={args} kwargs={kwargs}')
                func(*args, **kwargs)

            return wrapper_b

        return decorator_b


@decorator_maker(2)
def myfunc_c(*s, **d):
    print('myfunc_c:', s, d)


def myfunc_d(*s, **d):
    print('myfunc_d:', s, d)


# decorator_maker(2) возвращает функцию-декоратор, а затем ей передается уже
# наша декорируемая функция
myfunc_d = decorator_maker(2)(myfunc_d)


myfunc_c('1111', '2222', myvar='vars')
myfunc_d('1111', '2222', myvar='vars')
