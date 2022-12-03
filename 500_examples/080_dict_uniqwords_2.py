# подсчет количества слов в файлах с помощью defaultdict
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

        # замена пробелами игнорируемых символов
        for s in range(len(line)):
            if line[s] in ignorisym:
                line = line[:s] + ' ' + line[s + 1:]

        for word in line.lower().split():
            word = word.strip()
            if len(word) > 1:
                words[word] += 1

for word in sorted(words.items(), key=lambda i: i[1], reverse=True):
    print("{:30} occurs {} times".format(word[0], word[1]))
