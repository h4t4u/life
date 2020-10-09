import random
import subprocess
import time
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-W", "--width", dest="width", type=int, metavar="WIDTH", help="Set window width", default=60)
parser.add_argument("-H", "--height", dest="height", type=int, metavar="HEIGHT", help="Set window height", default=20)
parser.add_argument("-d", "--delay", dest="delay", type=float, metavar="dT", help="Set iteration delay", default=1)

args = parser.parse_args()

HEIGHT_CONST = args.height
WIDTH_CONST = args.width
field = [0]
ITEMS = {0: ' ',
         1: '#',
         2: "\x1b[1;34m" + 'F' + "\x1b[0m",
         3: "\x1b[1;31m" + 's' + "\x1b[0m"}


def choose(i):
    if i == 1:
        return 1
    if i == 2 or i == 4:
        return 2
    if i == 3 or i == 5:
        return 3
    return 0


def fillfield():
    result = [0] * HEIGHT_CONST
    for i in range(HEIGHT_CONST):
        result[i] = [choose(random.randint(0, 10)) for h in range(WIDTH_CONST)]
    return result


def countneighbours(i, j, type):
    c = 0
    for k in range(-1, 2):
        for d in range(-1, 2):
            if (k != 0 or d != 0) and (0 <= k+i < HEIGHT_CONST and 0 <= j+d < WIDTH_CONST):
                if field[i+k][j+d] == type:
                    c = c+1
    return c


def printfield():
    for k in field:
        s = ''
        for g in k:
            s = s + ITEMS[g]
        print(s)


def work():
    for i in range(HEIGHT_CONST):
        for j in range(WIDTH_CONST):

            if field[i][j] == 0:
                if countneighbours(i, j, 2) == 3:
                    field[i][j] = 2
                elif countneighbours(i, j, 3) == 3:
                    field[i][j] = 3

            if field[i][j] == 2:
                if countneighbours(i, j, 2) < 2 or countneighbours(i, j, 2) > 3:
                    field[i][j] = 0

            if field[i][j] == 3:
                if countneighbours(i, j, 3) < 2 or countneighbours(i, j, 3) > 3:
                    field[i][j] = 0


field = fillfield()
printfield()
while True:
    printfield()
    print(ITEMS[1] + " - Rocks")
    print(ITEMS[2] + " - Fishes")
    print(ITEMS[3] + " - Shrimps")
    work()
    time.sleep(args.delay)
    subprocess.call('clear' if os.name =='posix' else 'cls')
