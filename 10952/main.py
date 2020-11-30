DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def solve(line):
    a, b = (int(i) for i in line.split())
    return a + b


def main():
    for line in sys.stdin:
        if line.strip() == "0 0":
            break
        ans = solve(line)
        print(ans)


if __name__ == "__main__":
    main()