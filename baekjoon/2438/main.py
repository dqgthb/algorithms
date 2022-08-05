DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def solve(line):
    n = int(line)

    for i in range(n):
        print('*' * (1+i))



def main():
    for line in sys.stdin:
        solve(line)


if __name__ == "__main__":
    main()