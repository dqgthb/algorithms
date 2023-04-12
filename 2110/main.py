# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path


def binarySearch(lo, hi, func):

    while lo < hi:
        mid = lo + hi >> 1
        # print(lo, mid, hi, func(mid))
        if func(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo


def canInstall(n):

    maxCount = 0

    candidate = 0
    for j in range(1, N):
        if arr[j] - arr[0] >= N:
            candidate = j - 1
            break

    for j in range(0, candidate + 1):
        prev = arr[j]
        cnt = 1
        for i in range(j + 1, N):
            curr = arr[i]

            if curr - prev >= n:
                cnt += 1
                prev = curr
        maxCount = max(maxCount, cnt)

    return True if maxCount >= C else False


def main() -> None:
    # sys.setrecursionlimit(10**9)
    global N, C, arr
    N, C = map(int, input().split())

    arr = [int(input()) for _ in range(N)]
    arr.sort()

    ans = binarySearch(0, 1000000001, canInstall)

    print(ans - 1)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
