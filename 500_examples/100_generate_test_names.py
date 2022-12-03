# генерирование случайных троек Имя-Фамилия-ГодРождения
import random


def get_names():
    forenames_ = []
    surnames_ = []
    # чтение из 2-х файлов, т.е. внешний цикл выполниться 2 раза
    for names, filenames in ((forenames_, '100_IN_forenames.txt'), (surnames_, '100_IN_surnames.txt')):
        for line in open(filenames, encoding='utf8'):
            names.append(line.rstrip())
    return forenames_, surnames_


forenames, surnames = get_names()
years = list(range(1970, 2021)) * 3
limit = 100

# получить список из 5 неповторяющихся элементов random.sample(range(10), 5)
# получить список из 15 неповторяющихся элементов random.sample(tuple(range(10))*2, 15)
# хотя некоторые числа могут встречаться дважды, это различные элементы, ведь и в исходном кортеже их по 2-штуки

file = open('100_OUT.txt', 'w', encoding='utf8')
for year, forename, surname in zip(random.sample(years, limit),
                                   random.sample(forenames, limit),
                                   random.sample(surnames, limit)):
    name = '{} {}'.format(forename, surname)
    file.write('{:.<25}. {}\n'.format(name, year))
file.close()
