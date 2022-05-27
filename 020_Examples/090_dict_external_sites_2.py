import sys
from collections import defaultdict

# тоже самое но с помощью defaultdict
sites = defaultdict(set)
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
                    # применение словаря со значениями по умолчанию
                    # можно прямо обращаться по ключу, даже если такого ключа ещё нет
                    sites[site].add(filename)
                i = j
            else:
                break

for site in sorted(sites): 
    print("{0} is referred to in:".format(site)) 
    for filename in sorted(sites[site], key=str.lower): 
        print(" {0}".format(filename)) 
