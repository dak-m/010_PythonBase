
def bubblesort(arr_):
    # делаем копию что бы не испортить исходный список,
    # т.к. в питоне передача параметров происходит по ссылке
    sortarr = arr_[:]
    for i in range(len(sortarr)-1):
        for j in range(len(sortarr)-i-1):
            if sortarr[j] > sortarr[j+1]:
                sortarr[j], sortarr[j+1] = sortarr[j+1], sortarr[j]
    return sortarr


def medina(arr_):
    sortarr = bubblesort(arr_)
    i, j = divmod(len(sortarr), 2)
    if j == 0:
        medina_ = sum(sortarr[i-1:i+1])/2
    else:
        medina_ = sortarr[i]
    return medina_


try:
    arr = [int(s) for s in input('Числа: ').split()]
    print('Исходный: ', arr)
    print('Сортированный: ', bubblesort(arr))
    print('Медина = ', medina(arr))
    
except ValueError as err:
    print(err)


    