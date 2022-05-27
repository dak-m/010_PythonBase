# Пример параметров коммандной строки: maxwidth=5 format=*>12.2f 070_IN.csv 070_OUT.html

from sys import argv
from xml.sax.saxutils import escape


def process_options(options):

    if len(options) == 1 or options[1] in {'-h', '--help'}:
        print(f'usage: {options[0]} maxwidth=int format=str in.txt out.html')
        return None, None

    maxwidth, formatstr = 100, '.0f'

    for s in options[1:]:
        option = s.partition('=')
        if option[0] == 'maxwidth':
            maxwidth = int(option[2])
        elif option[0] == 'format':
            formatstr = option[2]
        else:
            pass

    return maxwidth, formatstr


def main():

    maxwidth, formatstr = process_options(argv)
    if (maxwidth, formatstr) == (None, None):
        return

    source, dest = argv[-2:]

    with open(source) as sourcefile, open(dest, 'w') as destfile:

        print_start(destfile)
        count = 0
        while True:
            line = sourcefile.readline()
            if line:
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, formatstr, destfile)
                count += 1
            else:
                break
        print_end(destfile)
        print("completed")


def print_start(destfile):
    destfile.write("<table border='1'>\n")


def print_end(destfile):
    destfile.write("</table>\n")


def print_line(line, color, maxwidth, formatstr, destfile):
    destfile.write("\t<tr bgcolor='{0}'>\n".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            destfile.write("\t\t<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                destfile.write("\t\t<td align='right'>{0:{1}}</td>\n".format(round(x), formatstr))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = escape(field)  # замена недопустимых символов & < > на '&amp;' '&lt;' '&gt;'
                if len(field) <= maxwidth:
                    destfile.write("\t\t<td>{0}</td>\n".format(field))
                else:
                    destfile.write("<td>{0:.{1}} ...</td>\n".format(field, maxwidth))
    destfile.write("\t</tr>\n")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:  # начало строки в кавычках
                quote = c
            elif quote == c:  # конец строки в кавычках
                quote = None
            else:
                field += c  # другая кавычка внутри строки в кавычках
            continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c  # добавить символ в поле
    if field:
        fields.append(field)  # добавить последнее поле в список
    return fields


main()
