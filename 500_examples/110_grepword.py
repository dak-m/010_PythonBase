# поиск слова по файлам, допустимо задавать маски фалов 0*.py
# пример использования enumerate
import glob
import sys

if len(sys.argv) < 3:
    print('error')
    sys.exit()

word = sys.argv[1]
for filenames in sys.argv[2:]:
    for filename in glob.glob(filenames):
        for linenumber, line in enumerate(open(filename, encoding='utf8'), start=1):
            if word in line:
                print('{}:{}:{:.40}'.format(filename, linenumber, line.strip()))
