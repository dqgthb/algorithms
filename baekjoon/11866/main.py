import os
import sys
import itertools
import collections
if os.path.exists("i"):
    sys.stdin = open("i")
if os.path.exists("a"):
    sys.stdout = open("o", "w")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def print_fast(st, end = "\n"):
    sys.stdout.write(st + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()


N, K = 0, 0
def main():
    N, K = (int(i) for i in input().split())
    dq = collections.deque(range(1, N+1))
    count = 0
    arr = []
    while len(dq) > 0:
        x = dq.popleft()
        count += 1
        if count != K:
            dq.append(x)
        else:
            arr.append(x)
            count = 0
    text = '<' + ', '.join(map(str, arr)) + '>'
    print_fast(text)


if __name__ == "__main__":
    main()