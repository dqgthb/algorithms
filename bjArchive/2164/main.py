import os
import sys
if os.path.exists("i"):
    sys.stdin = open("i")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def print_fast(st, end = ''):
    sys.stdout.write(st + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()


def main():
    import collections
    n = int(input().strip())
    q = collections.deque()
    for i in range(1, n+1):
        q.append(i)

    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())
    print(q.pop())


if __name__ == "__main__":
    main()