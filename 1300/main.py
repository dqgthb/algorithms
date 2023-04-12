# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from math import floor, sqrt
from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)
    global N, K

    N = int(input())
    K = int(input())

    # for i in range(1, 10):
    #     print(i, numbersLowerOrEqualTo(i))

    # arr = []
    # for i in range(1, N+1):
    #     for j in range(1, N + 1):
    #         arr.append(i*j)
    # arr.sort()
    # print(arr)

    # for i in range(1, 26):
    #     print(i, binarySearch(0, N * N + 1, i))

    print(binarySearch(0, N * N + 1, K))


# k 1 2 3 4 5 6 7 8 9
# v 1 2 2 3 3 4 6 6 9
# find ith
def binarySearch(lo, hi, num):

    while lo < hi:
        mid = lo + hi >> 1
        if numbersLowerOrEqualTo(mid) < num:
            lo = mid + 1
        else:
            hi = mid
    return lo


def test_print():
    arr = []
    for i in range(1, N):
        for j in range(1, N):
            arr.append(i * j)
    arr.sort()
    print(arr)


# if number is given, we can tell the index of it.
# that means, if we binary search the index, we can figure out the correct value.
# Let's say 100 is 7th and 140 is 9th. To figure out 8th, we binary search between 100 and 140.
def numbersLowerOrEqualTo(num):
    p = floor(sqrt(num))

    cnt = p * p

    # i * q + r = num
    for i in range(p + 1, N + 1):
        q, r = divmod(num, i)

        if q == 0:
            break

        cnt += 2 * q
    return cnt


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
