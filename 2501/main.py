# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path


def main() -> None:
    N, K = map(int, input().split())

    cnt = 0
    for i in range(1, N+1):
        if N % i == 0:
            cnt += 1

        if cnt == K:
            print(i)
            return

    print(0)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
