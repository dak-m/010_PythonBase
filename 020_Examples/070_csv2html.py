from sys import argv


def main():
    script, source, dest = argv

    with open(source) as sourcefile, open(dest, 'w') as destfile:
        maxwidth = 20
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
                print_line(line, color, maxwidth, destfile)
                count += 1
            else:
                break
        print_end(destfile)
        print("completed")


def print_start(destfile):
    destfile.write("<table border='1'>\n")


def print_end(destfile):
    destfile.write("</table>\n")


def print_line(line, color, maxwidth, destfile):
    destfile.write("\t<tr bgcolor='{0}'>\n".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            destfile.write("\t\t<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                destfile.write("\t\t<td align='right'>{0:d}</td>\n".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = escape_html(field)
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


def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


main()
