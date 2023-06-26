# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from collections import deque
from sys import stdin, argv
from os import path


D = ((-1, 0), (0, 1), (0, -1), (1, 0))


def main() -> None:
    # sys.setrecursionlimit(10**9)
    M, N = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]

    q = deque()

    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                q.append((i, j, 0))

    maxT = 0
    while q:
        i, j, t = q.popleft()
        maxT = max(maxT, t)

        for di, dj in D:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < M:
                if A[ni][nj] == 0:
                    A[ni][nj] = 1
                    q.append((ni, nj, t + 1))

    print(*A, sep="\n")

    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                print(-1)
                return
    print(maxT)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
