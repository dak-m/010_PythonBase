# сортировка
# key - функция, которая применяется к элементам, т.е. сортируются не сами элементы а резултьаты функции,
# хотя возвращается список содержащий исходные элементы
# это называется DSU = Decorate-Sort-Undecorate

w = ['ddd', 'aa', 'qq', 'bbb']
w.sort(key=str.lower)
print(w)
w.sort(key=len)
print(w)
w.sort(reverse=True)
print(w)

x = [(2, 'a'), (4, 'b'), (3, 'c'), (1, 'b')]
# по умолчанию сортировка идет по 1-ым элементам, если они равны то по вторым и т.д.
print(sorted(x))
# меняем местами порядок сортировки, т.е. сначала по буквам, потом по цифрам
print(sorted(x, key=lambda i: (i[1], i[0])))
# для кортежей с произвольным количеством элементов, т.е. по факту сортируются реверсированные кортежи
print(sorted(x, key=lambda i: tuple(j for j in reversed(i))))
# тоже самое, с помощью среза
print(sorted(x, key=lambda i: i[::-1]))

mix = ["1.3", -7.5, "5", 4, "-2.4", 1]
print(mix)
print(sorted(mix, key=float))
print(sorted(mix, key=lambda i: 0 if isinstance(i, str) else i))  # [0, -7.5, 0, 4, 0, 1]
