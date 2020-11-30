DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def main():
    max_ = -1
    idx = -1
    i = 1
    for line in sys.stdin:
        a = int(line.strip())
        if a > max_:
            max_ = a
            idx = i
        i += 1
    print(max_)
    print(idx)


if __name__ == "__main__":
    main()