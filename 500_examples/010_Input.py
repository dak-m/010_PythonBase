# Послать EOF: ctrl + d

total = 0
count = 0
while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as error:
        print(error)
        continue
    except EOFError as error:
        break
if count:
    print('count = ', count, 'total = ', total)
