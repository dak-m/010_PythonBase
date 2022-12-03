# Входной файл 120_IN.txt
import collections
import sys

ID, FNAME, MNAME, SNAME, DEP = range(5)

User = collections.namedtuple('User', 'username, fname, mname, sname, id')


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print('usage: {} file1 [file2 ... fileN]'.format(sys.argv[1]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding='utf8'):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.sname.lower(), user.fname.lower(), user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(':')
    username = generate_username(fields, usernames)
    user = User(username, fields[FNAME], fields[MNAME], fields[SNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    # fields[MNAME][:1] и fields[MNAME][0] это совнем ни одно и тоже!
    # в случае если fields[MNAME]='' (по условию отчество может быть не заполненным)
    # первый вариант отработает, а второй вызовет исключение IndexError
    username = ((fields[FNAME][0] + fields[MNAME][:1] + fields[SNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def print_users(users):
    namewidth = 17
    usernamewidth = 9
    columngap = " " * 2

    headline1 = "{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth)
    headline2 = "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth)

    header = (headline1 + columngap) * 3 + "\n" + (headline2 + columngap) * 3

    lines = []
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.mname:
            initial = " " + user.mname[0]
        name = "{0.sname}, {0.fname}{1}".format(user, initial)
        lines.append("{0:.<{nw}.{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth))

    lines_per_page = 64
    lino = 0
    for left, middle, right in zip(lines[::3], lines[1::3], lines[2::3]):
        if lino == 0:
            print(header)
        print(left + columngap + middle + columngap + right)
        lino += 1
        if lino == lines_per_page:
            print("\f")
            lino = 0


main()
