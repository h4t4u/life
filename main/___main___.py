import random
import os

HEIGHT_CONST = 10
WIDTH_CONST = 40
field = [0]
ITEMS = {0: ' ',
         1: '#',
         2: 's',
         3: 'F'}


def choose(i):
    if i == 1:
        return 1
    if i == 2:
        return 2
    if i == 3:
        return 3
    return 0


def fillfield():
    result = [0] * HEIGHT_CONST
    for i in range(HEIGHT_CONST):
        result[i] = [choose(random.randint(0, 30)) for i in range(WIDTH_CONST)]
    return result


def printfield():
    for k in field:
        for g in k:
            print(ITEMS[g], end='')
        print()


field = fillfield()
printfield()

