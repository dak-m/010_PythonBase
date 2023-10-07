numbers = []
while True:
    try:
        num = input('enter a number or Enter to finish: ')
        if not num:
            break 
        numbers.append(int(num))
    except ValueError as err:
        print(err)
    except EOFError:
        break
    
if numbers:
    print('numbers: ', numbers)
    count   = len(numbers)
    sum     = sum(numbers)
    lowest  = min(numbers)
    highest = max(numbers)
    mean    = sum/count
    print(f'count = {count} sum = {sum} lowest = {lowest} highest = {highest} mean = {mean}')
    