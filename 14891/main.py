from collections import deque
import sys
import os

spreadLeft = [[], [0], [1, 0], [2, 1, 0]]
spreadRight = [[1, 2, 3], [2, 3], [3], []]

TOP = 0
EAST = 2
WEST = 6


def printGear(gear):
    str_ = "WEST = {}, EAST = {}".format(gear[WEST], gear[EAST])
    print(str_)


def main():
    inputFile = sys.stdin

    if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
        inputFile = open(sys.argv[1])
    elif os.path.exists("i.txt"):
        inputFile = open("i.txt")

    with inputFile as f:
        gears = []

        for _ in range(4):
            gear = deque(map(int, f.readline().strip()))
            gears.append(gear)

        K = int(f.readline())

        for _ in range(K):
            idx, clockwise = map(int, f.readline().split())
            idx -= 1

            movements = [0] * 4
            movements[idx] = clockwise

            currIdx = idx
            for leftIdx in spreadLeft[idx]:
                if gears[leftIdx][EAST] != gears[currIdx][WEST]:
                    movements[leftIdx] -= movements[currIdx]
                    currIdx = leftIdx
                else:
                    break

            currIdx = idx
            for rightIdx in spreadRight[idx]:
                if gears[currIdx][EAST] != gears[rightIdx][WEST]:
                    movements[rightIdx] -= movements[currIdx]
                    currIdx = rightIdx
                else:
                    break

            for i in range(4):
                if movements[i] == 1:
                    gears[i].appendleft(gears[i].pop())
                elif movements[i] == -1:
                    gears[i].append(gears[i].popleft())

        sum_ = 0
        for i in range(4):
            if gears[i][0] == 1:
                sum_ += 2 ** i

        print(sum_)


if __name__ == "__main__":
    main()
