# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
import dataclasses
from os import path
from sys import stdin, argv
from collections import namedtuple
from dataclasses import dataclass
import logging
# logging.basicConfig(level=logging.DEBUG)

# from collections import deque
# from heapq import heappush, heappop
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br

D = ((-1, 0),
     (-1, -1),
     (0, -1),
     (1, -1),
     (1, 0),
     (1, 1),
     (0, 1),
     (-1, 1))

TEST = False


# Fish = namedtuple('Fish', 'id loc dir')

@dataclass
class Fish:
    id: int
    loc: tuple
    dir_: int

    def getForwardPosition(self, shark):
        i, j = self.loc
        dir_ = self.dir_
        di, dj = D[dir_]
        ni, nj = i + di, j + dj

        si, sj = shark.loc

        while not (0 <= ni < 4 and 0 <= nj < 4) or (ni == si and nj == sj):
            dir_ += 1
            dir_ %= 8
            di, dj = D[dir_]
            ni, nj = i + di, j + dj

        return ni, nj, dir_


def main() -> None:
    init()
    # sys.setrecursionlimit(10**9)

    # fishList = [None] * 16

    fishGrid = [[None] * 4 for _ in range(4)]

    for i in range(4):
        arr = list(map(int, input().split()))

        for j in range(4):
            k = j * 2
            fishNum, fishDir = arr[k], arr[k + 1]
            fishNum -= 1
            fishDir -= 1
            fish = Fish(id=fishNum, loc=(i, j), dir_=fishDir)
            # fishList[fishNum] = fish
            fishGrid[i][j] = fish

    if TEST:
        # print(*fishList, sep="\n")
        printFishGrid(fishGrid)

    playGame(fishGrid)

    print(maxScore)


def printFishGrid(fishGrid):
    # print(*fishGrid, sep="\n")
    if TEST:

        for i in range(4):
            for j in range(4):
                print(fishGrid[i][j].id if fishGrid[i]
                      [j] is not None else None, end=" ")
            print()


maxScore = -1


@dataclass
class Shark:
    loc: tuple
    dir_: int


def playGame(fishGrid):
    fish = eatFish(fishGrid, 0, 0)
    shark = Shark(loc=fish.loc, dir_=fish.dir_)
    moveShark(shark, fishGrid, fish.id + 1)


def eatFish(fishGrid, i, j):
    fish = fishGrid[i][j]
    logging.info(f'eathing {fish}')
    fishGrid[i][j] = None
    return fish


def moveFish(oldFishGrid, shark):
    fishGrid = [i[:] for i in oldFishGrid]

    for id in range(16):
        printFishGrid(fishGrid)
        fish = findFishById(fishGrid, id)
        if fish is not None:
            logging.info(f'{fish}')
            i, j = fish.loc
            ni, nj, nd = fish.getForwardPosition(shark)

            if fishGrid[ni][nj] is not None:
                swapFish(fishGrid, i, j, nd, ni, nj)
            else:
                fishGrid[i][j] = None
                newFish = dataclasses.replace(fish)
                newFish.loc = (ni, nj)
                newFish.dir_ = nd
                fishGrid[ni][nj] = newFish

    printFishGrid(fishGrid)

    return fishGrid


def swapFish(fishGrid, i, j, d, ni, nj):
    a = dataclasses.replace(fishGrid[i][j])
    a.loc = (ni, nj)
    a.dir_ = d
    b = dataclasses.replace(fishGrid[ni][nj])
    b.loc = (i, j)
    fishGrid[i][j] = b
    fishGrid[ni][nj] = a


def findFishById(fishGrid, id):
    for i in range(4):
        for j in range(4):
            fish: Fish | None = fishGrid[i][j]
            if fish is not None:
                if fish.id == id:
                    return fish
    return None


def getEdibleFish(shark, fishGrid):

    edibleFishList = []

    i, j = shark.loc
    di, dj = D[shark.dir_]
    ni, nj = i + di, j + dj

    while 0 <= ni < 4 and 0 <= nj < 4:
        if fishGrid[ni][nj] is not None:
            edibleFishList.append(fishGrid[ni][nj])
        ni, nj = ni + di, nj + dj

    return edibleFishList


def moveShark(shark, fishGrid, score):
    global maxScore

    logging.info(f'{score=}')

    fishGrid = moveFish(fishGrid, shark)

    edibleFish = getEdibleFish(shark, fishGrid)
    if not edibleFish:
        maxScore = max(maxScore, score)
        return

    for fish in edibleFish:
        fishGridCopy = [i[:] for i in fishGrid]
        eatFish(fishGridCopy, *fish.loc)
        sharkMoved = Shark(loc=fish.loc, dir_=fish.dir_)
        moveShark(sharkMoved, fishGridCopy, score + fish.id + 1)


def init() -> None:
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline


if __name__ == "__main__":
    main()
