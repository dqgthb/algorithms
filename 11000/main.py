from sys import stdin, argv
from heapq import heappush, heappop


def main() -> None:
    N = int(input())

    inTime = []
    outTime = []
    for _ in range(N):
        s, t = map(int, input().split())
        inTime.append(s)
        outTime.append(t)

    inTime.sort()
    outTime.sort()
    inTime.append(10**9 + 1)
    outTime.append(10**9 + 1)

    maxCnt = 0
    cnt = 0

    inIdx, outIdx = 0, 0

    while inIdx < N:
        while outTime[outIdx] <= inTime[inIdx]:
            outIdx += 1
            cnt -= 1

        inIdx += 1
        cnt += 1
        maxCnt = max(maxCnt, cnt)

    print(maxCnt)


if __name__ == "__main__":
    input = stdin.readline  # by default

    if len(argv) == 1:
        from os import path

        if path.isfile("i"):
            stdin = open("i")
            input = stdin.readline

    elif len(argv) == 2:
        stdin = open(argv[1])
        input = stdin.readline

    main()
