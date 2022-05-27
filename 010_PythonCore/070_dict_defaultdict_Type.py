import os
import collections

d1 = {'id':123, 'name':'julia'}
d2 = dict({'id':123, 'name':'julia'})
d3 = dict(id = 123, name = 'julia')
d4 = dict([('id', 123), ('name', 'julia')])
d5 = dict(zip(('id', 'name'), (123, 'julia')))
d6 = dict.fromkeys((1, 2, 3), 'default')


d1['color'] = 'red'
print(d1['color'])

# извлечь элемент с заданным ключем
print(d1.pop('color'))

# извлечь первопопавшийся элемент
print(d1.popitem())

# получить элемент с заданным ключем, если его нет то создать(!) с заданным ключем/значением
# и затем его уже вернуть
print(d3.setdefault('id', 333))
print(d3.setdefault('idd', 333))

# добавление с заменой существующих
d2.update([('color', 'red'), ('name', 'lisa')]) 

# обход
# items() возвращает представление в виде списка кортежей (ключ, значение)
for item in d2.items():
    print(item[0], item[1])

for key, value in d2.items():
    print(key, value)

# обход значений
for value in d2.values(): 
    print(value)

# обход ключей
for key in d2.keys(): 
    print(key)
    
for key in d2:
    print(key)
    
# items(), values(), keys() возвращают представление словаря
pd2 = d2.items()
print(pd2)
# при изменении словаря представление меняется автоматом
d2['class'] = 1
print(pd2)

# для представлений доступны операции как над множествами |&^-
# определить какие есть ключи из заданных
pk2 = d2.keys()
s = {'name', 'color', 'age'}
k = pk2 & s

# генераторы словарей
file_sizes = {name: os.path.getsize(name) for name in os.listdir()
    if os.path.isfile(name)} 

# инверсия словаря
inverted_d3 = {v: k for k, v in d3.items()}
inverted_inverted_d3 = {i[1]: i[0] for i in inverted_d3.items()}

# инициализация defaultdict с помощью лямбды
# int следует понимать как ссылку на конструктор int()
int_dict = collections.defaultdict(int)
print(int_dict['zero'])
point_zero_dict = collections.defaultdict(lambda: (0, 0))
print(point_zero_dict['point 1'])


