#1. Сгенерируйте с использованием функции range (случайный шаг от 3 до 5)
#массив, содержащий отсортированные числа от 10 до 250 млн.
#Можно использовать функцию randomint из модуля random для ещё большей
#рандомизации значений, но для целей работы алгоритма бинарного поиска
#проследите, чтобы значения в массиве были отсортированы.
#2. Сгенерируйте с помощью list comprehensions и функции randomint
#(встроенный модуль random) 10 случайных чисел.
#3. Напишите функцию для алгоритма линейного поиска.
#4. Напишите функцию для алгоритма бинарного поиска.
#5. Проверьте наличие ранее сгенерированных случайных чисел в массиве с
#помощью алгоритмов линейного и бинарного поиска, замерьте время

import random
lst = []
results = {}
a = list(range(10, 250000000, 3))
for i in range(10):
    lst.append(random.randint(10, 250000000))

#примерно 15с
def linsearch(a, element, listlen):
    for i in range(0, listlen):
        if a[i] == element:
            return(i)
    return('not found')

#примерно 1,5с
def binsearch(a, element):
    low = 0
    high = len(a) - 1
    while low <= high:
        middle = (low + high) // 2
        if a[middle] == element:
            return(middle)
        elif a[middle] > element:
            high = middle - 1
        else:
            low = middle + 1
    return('not found')

listlen = len(a)
for i in lst:
    results[i] = binsearch(a, i)

print(results)