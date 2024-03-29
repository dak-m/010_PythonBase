def decorator_with_args(decorator_to_enhance):
    """
    Эта функция задумывается КАК декоратор и ДЛЯ декораторов.
    Она должна декорировать другую функцию, которая должна быть декоратором.
    Лучше выпейте чашку кофе.
    Она даёт возможность любому декоратору принимать произвольные аргументы,
    избавляя Вас от головной боли о том, как же это делается, каждый раз,
    когда этот функционал необходим.
    """
 
    # Мы используем тот же трюк, который мы использовали для передачи
    # аргументов:
    def decorator_maker(*args, **kwargs):
 
        # создадим на лету декоратор, который принимает как аргумент только 
        # функцию, но сохраняет все аргументы, переданные своему "создателю"
        def decorator_wrapper(func):
 
            # Мы возвращаем то, что вернёт нам изначальный декоратор,
            # который, в свою очередь ПРОСТО ФУНКЦИЯ (возвращающая функцию).
            # Единственная ловушка в том, что этот декоратор должен быть
            # именно такого decorator(func, *args, **kwargs) вида,
            # иначе ничего не сработает
            return decorator_to_enhance(func, *args, **kwargs)
 
        return decorator_wrapper
 
    return decorator_maker


# Мы создаём функцию, которую будем использовать как декоратор и декорируем
# её. Не стоит забывать, что она должна иметь вид "decorator(func, *args,
# **kwargs)"
@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print("Мне тут передали...:", args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper


# Теперь декорируем любую нужную функцию нашим новеньким, ещё блестящим
# декоратором:
@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print("Привет", function_arg1, function_arg2)


decorated_function("Вселенная и", "всё прочее")