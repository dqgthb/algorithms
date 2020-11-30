DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def solve(n):
    import collections
    cnt = collections.Counter(int(i) for i in str(n))
    for i in range(10):
        print(cnt[i])


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solve(a * b * c)


if __name__ == "__main__":
    main()