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
    global R, C, A, N, T
    R, C = map(int, input().split())

    A = [[i for i in input().strip()] for _ in range(R)]

    N = int(input())

    T = [int(i) for i in input().split()]

    for i, e in enumerate(T):
        throw(i, e)
        # print(*A, sep="\n")
        # print()

    for row in A:
        print(''.join(row))


def throw(turn, height):
    r = R - height
    if turn % 2 == 0:

        for i, e in enumerate(A[r]):
            if e == 'x':
                A[r][i] = '.'
                gravity(r, i)
                break
    else:
        for i, e in reversed(list(enumerate(A[r]))):
            if e == 'x':
                A[r][i] = '.'
                gravity(r, i)
                break


def gravity(r, i):

    for x, y in D:
        nx = r + x
        ny = i + y

        cluster = findCluster(nx, ny)
        if not cluster:
            continue

        # bottoms = findBottoms(cluster)

        height = getHowMuchShouldClusterFall(cluster)

        if height == 0:
            continue
        else:
            shiftDown(cluster, height)
            return


def shiftDown(cluster, height):
    for x, y in cluster:
        A[x][y] = '.'

    for x, y in cluster:
        A[x + height][y] = 'x'


def getHowMuchShouldClusterFall(cluster):

    min_ = 101
    clusterSet = set(cluster)

    for i, j in clusterSet:

        # j column

        for ni in range(i + 1, R):
            if A[ni][j] == 'x':
                if (ni, j) in clusterSet:
                    continue
                min_ = min(min_, ni - i - 1)
                break
        else:
            min_ = min(min_, R - i - 1)

    return min_


def findBottoms(cluster):
    bottomCandidates = [-1] * C

    for i, j in cluster:
        bottomCandidates[j] = max(bottomCandidates[j], i)

    bottoms = [(bottomCandidates[i], i)
               for i in range(C) if bottomCandidates[i] != -1]
    return bottoms


D = ((-1, 0),
     (0, -1),
     (0, 1),
     (1, 0))


def findCluster(i, j):

    cluster = []
    if i < 0 or i >= R or j < 0 or j >= C:
        return cluster

    if A[i][j] == '.':
        return cluster

    visited = [[False for _ in range(C)] for _ in range(R)]
    dq = deque([(i, j)])
    visited[i][j] = True
    cluster.append((i, j))

    while dq:
        r, c = dq.popleft()

        for dr, dc in D:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < R and 0 <= nc < C:
                if A[nr][nc] == 'x':
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        cluster.append((nr, nc))
                        dq.append((nr, nc))

    return cluster


def testFindCluster():
    print(findCluster(4, 2))


def testFindBottoms():
    print(findBottoms(findCluster(4, 2)))


def testShiftDown():
    cluster = ((1, 2), (1, 3))
    shiftDown(cluster, -1)
    print(*A, sep='\n')


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
    # testFindCluster()
    # testFindBottoms()
    # testShiftDown()
