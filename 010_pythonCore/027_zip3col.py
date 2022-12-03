from itertools import zip_longest

# Вывод коллекции в 3-и колонки с помощью zip
t = list(range(1, 11))

# тут обычный zip даст ошибку!(точнее не выведет последние элементы) если
# количество элементов не кратно 3, то в срезах будет не одинаковое число
# элементов и zip будет равняться на наименьший по длине срез
for left, middle, right in zip_longest(t[::3], t[1::3], t[2::3], fillvalue=''):
    print('{:{lfiller}>5} {:{mfiller}>5} {:{rfiller}>5}'.format(
        left, middle, right,
        lfiller='_',
        mfiller='_' if middle != '' else '',
        rfiller='_' if right != '' else ''))
