import sys
import unicodedata


# поиск символа юникода по его имени
def print_unicode_table(words_):
    title = ('decimal', 'hex', 'chr', 'name')
    print('{:<7} {:<5} {:<3} {:^40}'.format(*title))
    print('{0:-<7} {0:-<5} {0:-<3} {0:-<40}'.format(''))

    code = ord(' ')
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, '*** unknown ***')

        flag = True
        if words_ is not None:
            for word in words_:
                if word.lower() not in name.lower():
                    flag = False
                    break

        if flag:
            print('{0:7} {0:5X} {0:^3c} {1}'.format(code, name.title()))
        code += 1


words = None
if len(sys.argv) > 1:
    if sys.argv[1] in ('-h', '--help'):
        # print('usage: {} [string]'.format(sys.argv[0])
        print('usage: {[0]} [string]'.format(sys.argv))
        words = 0
    else:
        words = sys.argv[1:]

if words:
    print_unicode_table(words)
