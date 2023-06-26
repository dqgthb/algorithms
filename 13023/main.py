# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)

    global N, M, G, V
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())

        G[a].append(b)
        G[b].append(a)

    for i in range(N):
        V = [False] * N
        V[i] = True
        if dfs(i, 1):
            print(1)
            return
    print(0)


def dfs(a, cnt):
    if cnt == 5:
        return True

    for b in G[a]:
        if not V[b]:
            V[b] = True
            if dfs(b, cnt + 1):
                return True
            V[b] = False
    return False


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
