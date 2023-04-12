# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from collections import deque
from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)
    global N, Q, G
    N, Q = map(int, input().split())

    G = [[] for _ in range(N)]

    for _ in range(N - 1):
        p, q, r = map(int, input().split())
        p -= 1
        q -= 1

        G[p].append((q, r))
        G[q].append((p, r))

    for _ in range(Q):
        k, v = map(int, input().split())
        v -= 1

        query(k, v)


def query(k, v):

    visited = [False] * N
    dq = deque([v])
    visited[v] = True

    cnt = 0
    while dq:
        vertex = dq.popleft()

        for node, cost in G[vertex]:
            if not visited[node]:
                visited[node] = True
                if cost >= k:
                    cnt += 1
                    dq.append(node)
    print(cnt)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
