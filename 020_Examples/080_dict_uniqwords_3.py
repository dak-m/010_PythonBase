# подсчет количества слов в файлах с помощью defaultdict
# пример параметра: 070_OUT.html
import sys
import string
import collections


def myint():
    return 0


# здесь int ссыска на фабричную функцию создания типа int()
# можно заменить на свою:
# words = collections.defaultdict(myint)
# либо передать лямбду
# words = collections.defaultdict(lambda :0)
words = collections.defaultdict(int)
ignorisym = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename, encoding="utf8"):

        # замена пробелами игнорируемых символов с помощью лямбды в генераторе
        # line = ''.join((lambda i: ' ' if i in ignorisym else i) (i) for i in line)
        # но оказалось можно и без лямбды...)
        line = ''.join(' ' if i in ignorisym else i for i in line)

        for word in line.lower().split():
            word = word.strip()
            if len(word) > 1:
                # в этом и есть прелесть defaultdict, просто обращаемся к ключу не проверяя его наличие                 
                words[word] += 1

# сортировка слов по частоте с которой они встречаются
for word in sorted(words.items(), key=lambda i: i[1], reverse=True):
    print("{:30} occurs {} times".format(word[0], word[1]))
