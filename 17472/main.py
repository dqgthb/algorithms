# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
import heapq
from sys import stdin, argv
from os import path

# from collections import deque
# from heapq import heappush, heappop
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


def main() -> None:
    # sys.setrecursionlimit(10**9)
    global N, M, G
    N, M = map(int, input().split())

    G = [list(int(i) for i in input().split()) for _ in range(N)]

    # print(*G, sep='\n')

    islands = detectIslands([i[:] for i in G])

    pq = []
    numIsland = len(islands)
    for i in range(numIsland):
        for j in range(i + 1, numIsland):
            distance = distanceBetweenIslands(islands[i], islands[j])
            # print("distance!:", distance, i, j)
            if distance == 10 ** 9:
                continue
            pq.append((distance, i, j))

    heapq.heapify(pq)

    while pq and pq[0][0] == 1:
        heapq.heappop(pq)

    # print(pq)

    global P
    P = [i for i in range(numIsland)]

    count = 0
    totalDistance = 0
    while pq and count < numIsland - 1:
        distance, x, y = heapq.heappop(pq)
        # print(distance, x, y)
        if union(x, y):
            count += 1
            totalDistance += distance

    if count != numIsland - 1:
        print(-1)
    else:
        print(totalDistance)


def find(x):
    while P[x] != x:
        x = P[x]
    return x


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return False

    if px < py:
        P[py] = px
    else:
        P[px] = py
    return True


D = ((1, 0), (-1, 0), (0, 1), (0, -1))


def detectIslands(G):
    islands = []

    for i in range(N):
        for j in range(M):
            if G[i][j] == 1:
                island = [(i, j)]

                stack = [(i, j)]
                G[i][j] = 0

                while stack:
                    x, y = stack.pop()

                    for dx, dy in D:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < N and 0 <= ny < M:
                            if G[nx][ny] == 1:
                                G[nx][ny] = 0

                                island.append((nx, ny))
                                stack.append((nx, ny))
                islands.append(island)
    return [set(i) for i in islands]


def distanceBetweenIslands(a, b):

    min_ = 10 ** 9 + 1
    for x, y in a:
        for z, w in b:
            if x == z:
                d = abs(y - w)
                if d <= 2:
                    continue

                if canInstallVertical(a, b, x, y, w):
                    min_ = min(min_, d)

            elif y == w:
                d = abs(x - z)
                if d <= 2:
                    continue
                if canInstallHorizontal(a, b, y, x, z):
                    min_ = min(min_, d)
    return min_ - 1


def canInstallHorizontal(a, b, x, y, z):

    if y > z:
        y, z = z, y

    for i in range(y + 1, z):
        if G[i][x] == 1:
            return False

    return True


def canInstallVertical(a, b, x, y, z):

    if y > z:
        y, z = z, y

    for i in range(y + 1, z):
        if G[x][i] == 1:
            return False

    return True


def testDistanceBetweenIslands():
    copyG = [i[:] for i in G]

    x = detectIslands(copyG)
    distance = distanceBetweenIslands(x[0], x[1])
    print(distance)


def testDetectIslands():
    copyG = [i[:] for i in G]

    x = detectIslands(copyG)
    print(*x, sep="\n")


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()

    # testDetectIslands()
    # testDistanceBetweenIslands()
