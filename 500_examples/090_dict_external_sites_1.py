import sys

# структура словаря такая: ключи - имена сайтов,
# значения - множество имен файлов, где оно встречается
sites = {}
for filename in sys.argv[1:]:
    for line in open(filename, encoding="utf8"):
        i = 0
        while True:
            site = None
            i = line.find('http://', i)
            if i > -1:
                i += len('http://')
                for j in range(i, len(line)):
                    if not (line[j].isalnum() or line[j] in '.-'):
                        site = line[i:j].lower()
                        break
                if site and '.' in site:
                    # добаление данных в словарь, если значение словаря - это коллекция,
                    # то очень удобно добавлять в неё элементы так
                    # sites.setdefault(site, set()) возвращает значение словаря по ключу,
                    # если его нет, то оно будет создано с помощью set() и возвращено
                    # после чего в созданное множество добавляется filename
                    sites.setdefault(site, set()).add(filename)
                i = j
            else:
                break

for site in sorted(sites): 
    print("{0} is referred to in:".format(site)) 
    for filename in sorted(sites[site], key=str.lower): 
        print(" {0}".format(filename)) 
