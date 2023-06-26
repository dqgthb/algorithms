# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from collections import deque
from sys import stdin, argv
from os import path

# from collections import deque
# from heapq import heappush, heappop
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


def main() -> None:
    # sys.setrecursionlimit(10**9)
    global W, H, G

    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        G = [[i for i in input().strip()] for _ in range(H)]
        solve()


def solve():
    # testDistanceFromXtoY()
    # print(dirtySlots)

    solution()


def solution():
    global robot, dirtySlots
    robot = getRobotPosition(G)
    dirtySlots = getDirtySlots(G)
    global dirtyNum
    dirtyNum = len(dirtySlots)

    distanceToDirtySlots = [distanceFromXtoY(robot, i) for i in dirtySlots]

    if -1 in distanceToDirtySlots:
        print(-1)
        return

    global distanceBetween
    distanceBetween = getDistanceBetweenAllDirtlyPoints(dirtySlots)

    # print(*distanceBetween, sep='\n')

    min_ = 10 ** 9
    visited = [False for _ in range(dirtyNum)]
    for i, e in enumerate(dirtySlots):
        visited[i] = True
        totalDistance = dfs(i, visited, distanceToDirtySlots[i])
        visited[i] = False
        min_ = min(min_, totalDistance)
    print(min_)


def dfs(dirtySpotIdx, visited, cumulativeDistance):
    if all(visited):
        return cumulativeDistance

    minDistance = 10 ** 9
    for i, e in enumerate(dirtySlots):
        if not visited[i]:
            visited[i] = True
            totalDistanceOfThisPath = dfs(i, visited,
                                          cumulativeDistance + distanceBetween[dirtySpotIdx][i])
            minDistance = min(minDistance, totalDistanceOfThisPath)
            visited[i] = False
    return minDistance


def getDistanceBetweenAllDirtlyPoints(dirtySlots):
    n = len(dirtySlots)

    distanceMatrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            distance = distanceFromXtoY(dirtySlots[i],
                                        dirtySlots[j])
            distanceMatrix[i][j] = distance
            distanceMatrix[j][i] = distance

    return distanceMatrix


def testDistanceFromXtoY():
    distance = distanceFromXtoY((1, 3), (1, 12))
    print(distance)


D = ((0, 1), (0, -1), (1, 0), (-1, 0))


def distanceFromXtoY(x, y):
    visited = [[False for _ in range(W)] for _ in range(H)]

    xi, xj = x
    yi, yj = y

    dq = deque([(xi, xj, 0)])
    visited[xi][xj] = True

    while dq:
        i, j, distance = dq.popleft()

        for di, dj in D:
            ni, nj = i + di, j + dj

            if ni == yi and nj == yj:
                return distance + 1

            if 0 <= ni < H and 0 <= nj < W:
                if not visited[ni][nj]:
                    visited[ni][nj] = True

                    if G[ni][nj] != 'x':
                        dq.append((ni, nj, distance + 1))
    return -1


def getDirtySlots(G):
    slots = []
    for i in range(H):
        for j in range(W):
            if G[i][j] == '*':
                slots.append((i, j))
    return slots


def getRobotPosition(G):
    for i in range(H):
        for j in range(W):
            if G[i][j] == 'o':
                return i, j
    raise RuntimeError("robot must exists.")


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
