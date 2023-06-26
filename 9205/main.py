from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)
    T = int(input())

    for t in range(T):
        n = int(input())

        if solution(n):
            print("happy")
        else:
            print("sad")


def solution(n):
    N = n + 2
    O = [tuple(map(int, input().split())) for _ in range(N)]

    G = [[] for _ in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            x, y = O[i]
            xx, yy = O[j]

            if abs(x - xx) + abs(y - yy) <= 1000:
                G[i].append(j)
                G[j].append(i)

    stack = [0]
    V = [False for _ in range(N)]
    V[0] = True

    while stack:
        x = stack.pop()

        for g in G[x]:
            if g == N - 1:
                return True
            if not V[g]:
                V[g] = True
                stack.append(g)

    return False


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
