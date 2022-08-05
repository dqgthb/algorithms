DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def solve(line):
    line = line.strip()
    count = 0
    sum_ = 0
    for c in line:
        if c == "O":
            count += 1
            sum_ += count
        else:
            count = 0
    return sum_


def main():
    t = input()
    for line in sys.stdin:
        ans = solve(line)
        print(ans)


if __name__ == "__main__":
    main()