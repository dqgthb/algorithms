from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)

    global N, O
    N = int(input())

    O = [list(input().strip()) for _ in range(N)]

    places = [(i, j) for i in range(N) for j in range(N) if O[i][j] == "."]

    print(places)

    max_ = 0
    loc = None

    for i, j in places:
        n = flipStone(i, j)

        if max_ < n:
            max_ = n
            loc = (i, j)

    nO = [i[:] for i in O]

    test()


def flipStone(O, i, j):
    if not canPlace(i, j):
        return 0


def test_flipStone():
    O = [list[i] for i in (".B.", ".W.", "...")]
    flipStone(O, 0, 0)


def test_canPlace():


def test():
    O = [list[i] for i in (".B.", ".W.", "...")]
    test_flipStone()
    test_canPlace()


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    # main()
    test()
