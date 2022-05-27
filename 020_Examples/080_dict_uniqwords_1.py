# подсчет количества слов в файлах
import sys
import string

words = {}
ignorisym = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(ignorisym)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1

for word in sorted(words):
    print("{:30} occurs {} times".format(word, words[word]))

# частота вхождения слов по возрастанию
print('='*50)
for word in sorted(words.items(), key=lambda i: i[1]):
    print("{:30} occurs {} times".format(word[0], word[1]))

# частота вхождения слов по убыванию
print('='*50)
for word in sorted(words.items(), key=lambda i: i[1], reverse=True):
    print("{:30} occurs {} times".format(word[0], word[1]))
