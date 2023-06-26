import os
import sys

PLAYER = -1
EXIT = -1234

totalDistance = 0


def main():
    global N, M, K

    N, M, K = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        A[a][b] += PLAYER

    ei, ej = map(int, input().split())
    ei -= 1
    ej -= 1

    A[ei][ej] = EXIT

    # print(*A, sep="\n")

    for k in range(K):
        # print("\ntime=", k + 1)
        players = getPlayers(A)
        ei, ej = getExit(A)
        sortPlayers(players, ei, ej)
        movePlayers(A, players, ei, ej)

        # print("after move")
        # print(*A, sep="\n")

        players = getPlayers(A)
        if len(players) == 0:
            break
        r, c, size = findRotatingArea(A, ei, ej, players)
        decreaseDurability(A, r, c, size)
        rotate(A, r, c, size)

        # print("after rotate")
        # print(*A, sep="\n")

    print(totalDistance)
    print(*(i + 1 for i in getExit(A)))


def movePlayers(A, players, ei, ej):
    for pi, pj in players:
        movePlayer(A, pi, pj, ei, ej)


D = ((-1, 0), (1, 0), (0, -1), (0, 1))


def movePlayer(A, i, j, ei, ej):
    global totalDistance
    distance = getDistance(i, j, ei, ej)

    for di, dj in D:
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < N:
            if A[ni][nj] == EXIT:
                totalDistance -= A[i][j]
                A[i][j] = 0
                return
            elif A[ni][nj] <= 0:  # if empty or player
                nd = getDistance(ni, nj, ei, ej)
                if distance - 1 == nd:
                    totalDistance -= A[i][j]
                    A[ni][nj] += A[i][j]
                    A[i][j] = 0
                    return


def getDistance(a, b, x, y):
    return abs(a - x) + abs(b - y)


def getPlayers(A):
    return [(i, j) for i in range(N) for j in range(N) if -10 <= A[i][j] < 0]


def sortPlayers(players, ei, ej):
    players.sort(key=lambda p: getDistance(p[0], p[1], ei, ej))


def getExit(A):
    for i in range(N):
        for j in range(N):
            if A[i][j] == EXIT:
                return i, j


def findRotatingArea(A, x, y, players):
    size = 10**9
    for pi, pj in players:
        size = min(size, max(abs(pi - x), abs(pj - y)))
    size += 1

    for i in range(size):
        for j in range(size):
            r, c = x - size + 1 + i, y - size + 1 + j

            if 0 <= r and 0 <= c and r + size - 1 < N and c + size - 1 < N:
                for pi, pj in players:
                    if 0 <= pi - r < size and 0 <= pj - c < size:
                        return r, c, size
    raise Exception("no player found inside rotating area.")


def findRotatingAreaV1_NOT_USED_ANYMORE(A, x, y, players):
    for size in range(2, N):
        for i in range(size):
            for j in range(size):
                r, c = x - size + 1 + i, y - size + 1 + j

                if 0 <= r and 0 <= c and r + size - 1 < N and c + size - 1 < N:
                    for pi, pj in players:
                        if 0 <= pi - r < size and 0 <= pj - c < size:
                            return r, c, size
    return None


def decreaseDurability(A, x, y, size):
    for i in range(size):
        for j in range(size):
            if A[x + i][y + j] > 0:
                A[x + i][y + j] -= 1


def rotate(A, x, y, size):
    temp = [[None for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            temp[i][j] = A[x + i][y + j]

    for i in range(size):
        for j in range(size):
            A[x + j][y + size - 1 - i] = temp[i][j]


def test_rotate():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(*A, sep="\n")

    rotate(A, 0, 0, 3)

    print(*A, sep="\n")


def test_decreaseDurability():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    decreaseDurability(A, 1, 1, 2)
    print(*A, sep="\n")


def test_findRotatingArea():
    A = """0 0 0 0 1
    9 2 2 0 0
    0 1 0 1 0
    0 0 0 1 0
    0 0 0 0 0"""

    A = [[int(i) for i in i.split()] for i in A.split("\n")]
    players = [(0, 2), (2, 0), (2, 4)]
    x = findRotatingArea(A, 2, 2, players)
    print(x)


def test_movePlayer():
    A = """0 0 0 0 1
    9 2 -1 0 0
    -1 1 -2 1 0
    0 0 0 1 0
    0 0 -1 0 0"""

    A = [[int(i) for i in i.split()] for i in A.split("\n")]
    movePlayer(A, 2, 0, 2, 2)
    movePlayer(A, 4, 2, 2, 2)
    movePlayer(A, 1, 2, 2, 2)
    print(*A, sep="\n")


def test():
    # test_rotate()
    # test_decreaseDurability()
    # test_findRotatingArea()
    # test_movePlayer()
    pass


if __name__ == "__main__":
    global input
    input = sys.stdin.readline
    if len(sys.argv) == 2:
        input = open(sys.argv[1]).readline
    elif os.path.isfile("i"):
        input = open("i").readline

    main()
    test()
