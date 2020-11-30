import os
import collections
import sys
if os.path.exists("i"):
    sys.stdin = open("i")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def print_fast(st, end = "\n"):
    sys.stdout.write(st + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()


def main():
    N = int(input().strip())
    cards = get_ints()
    M = (int(i) for i in input().split())
    have = get_ints()

    c = collections.Counter(cards)

    arr = [str(c[i]) for i in have]
    print(' '.join(arr))




if __name__ == "__main__":
    main()