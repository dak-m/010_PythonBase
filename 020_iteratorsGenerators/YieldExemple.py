# Любая функция в Python, в теле которой встречается ключевое слово yield,
# называется генераторной функцией — при вызове она возвращает объект-генератор.
# Объект-генератор реализует интерфейс итератора, соответственно с этим объектом можно работать,
# как с любым другим итерируемым объектом.

# 1. при вызове функции gen_fun создается объект-генератор
# 2. for вызывает iter() с этим объектом и получает итератор этого генератора
# 3. в цикле вызывает функция next() с этим итератором пока не будет получено исключение StopIteration
# 4. при каждом вызове next выполнение в функции начинается с того места
#    где было завершено в последний раз и продолжается до следующего yield

# Похоже на игру в пинг-понг, функции вызывают друг друга по очереди, но начать должна вызывающая программа
# И при первом стартовом вызове ничего передать с помощью send() нельзя


def generator_function():
    
    print('== inside generator start')
    send_value = yield 0  # вернуть 0 в вызывающую программу и ждать(!!!) от неё вызова
    # когда она сделает вызов с помощью send(X),
    # то X поместить в send_value и продолжить выполнение далее по коду (до следующего Yield)
    # если вызов сделан с помощью next(), то в send_value поместить None

    gen_value = 1
    print('== inside generator gen_value = {0} send_value = {1}'.format(gen_value, send_value))
    send_value = yield gen_value

    gen_value = 2
    print('== inside generator gen_value = {0} send_value = {1}'.format(gen_value, send_value))
    send_value = yield gen_value

    print('== inside generator end')
    # StopIteration


mygenerator = generator_function()
# myiterator = iter(mygenerator) # он же и итератор

# пока генератор не стартован next()'ом, послать ему через send() можно только None
i = mygenerator.send(None)  # <=> i = next(myiterator)
print('return yeild = {0}'.format(i))

i = mygenerator.send(1)
print('return yeild = {0}'.format(i))
          
i = mygenerator.send(2)
print('return yeild = {0}'.format(i))

i = mygenerator.send(3)
print('return yeild = {0}'.format(i))
