DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def solve(line):
    arr = [int(i) for i in line.split()]
    if arr == sorted(arr):
        return "ascending"
    elif arr == sorted(arr, reverse=True):
        return "descending"
    else:
        return "mixed"


def main():
    for line in sys.stdin:
        ans = solve(line.strip())
        print(ans, end='')



if __name__ == "__main__":
    main()