# множества являются ИЗМЕНЯЕМЫМИ, НЕ УПОРЯДОЧЕННЫМИ(не возможно обратиться по индексу) коллекиями.
# Итерируемы, но порядок произволен. Множества могут содержат только НЕИЗМЕНЯЕМЫЕ объекты
# frozenset - НЕИЗМЕНЯЕМЫЕ множества

s1 = {1, 2, 3}
s2 = {1, 4}

print('{} or  {} = {} <=> {}'.format(s1, s2, s1 | s2, s1.union(s2)))
print('{} and {} = {} <=> {}'.format(s1, s2, s1 & s2, s1.intersection(s2)))
print('{} -   {} = {} <=> {}'.format(s1, s2, s1 - s2, s1.difference(s2)))
print('{} xor {} = {} <=> {}'.format(s1, s2, s1 ^ s2, s1.symmetric_difference(s2)))

# отсутствуют общие элементы?
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s2 - {1}))

# сравнение множеств
print({1, 2, 3} >= {1, 3})

# s1.update(s2)  
s1 |= s2

# s1.intersection_update(s2)
s1 = {1, 2, 3}
s2 = {1, 4}
s1 &= s2

# s1.difference_update(s2)
s1 = {1, 2, 3}
s2 = {1, 4}
s1 -= s2

# s1.symmetric_difference_update(s2)
s1 = {1, 2, 3}
s2 = {1, 4}
s1 ^= s2

# очистка списка от дубликатов
li = [1, 2, 2, 3, 4, 5]
li = list(set(li))

# удаление "ненужных" элементов из множества(списка)
li = list(set(li) - {2, 3})

# фильтрация "нужных" элементов без повторяющихся
files = ['1.htm', '1.html', '1.htm', '1.jpg']
html = {x for x in files if x.lower().endswith((".htm", ".html"))} 
