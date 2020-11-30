DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def main():
    n = int(input().strip())
    for i in range(n, 0, -1):
        print(i)


if __name__ == "__main__":
    main()