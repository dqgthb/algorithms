# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
import math
from sys import stdin, argv
from os import path


def main() -> None:

    # sys.setrecursionlimit(10**9)
    N = int(input())

    # inputs.sort(key=lambda x: x[1])
    p = [list(map(int, input().split())) for _ in range(N)]

    p.sort(key=lambda x: x[0])  # must sort by y, and if same by x
    p.sort(key=lambda x: x[1])
    minPoint = p[0]  # smallest y
    # minPoint = min(p, key=lambda x: x[1])

    p.sort(key=lambda x: getAngle(minPoint, x))
    # print(p)

    stack = [p[0], p[1]]

    for point in p[2:]:
        x, y = point

        while True:
            # print(stck)
            if len(stack) == 1:
                stack.append(point)
                break

            if CCW(stack[-2], stack[-1], point) > 0:
                stack.append(point)
                break
            else:
                x = stack.pop()

    if CCW(stack[-2], stack[-1], stack[0]) <= 0:
        stack.pop()

    # print(*stack, sep="\n")
    print(len(stack))


def getAngle(a, b):
    ax, ay = a
    bx, by = b

    val = math.atan2(by - ay, bx - ax)
    # print(a, b, val)
    return val


def CCW(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c

    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)


def testCCW():
    a = (1, 1)
    b = (3, 1)
    c = (2, 1)

    print(CCW(a, b, c))


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
    # testCCW()
