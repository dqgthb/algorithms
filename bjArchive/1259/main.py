import os.path
DEBUG = False
if os.path.exists("i"):
    DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def isPalindrome(st: str):
    mid = len(st)//2
    len_ = len(st)
    for i, e in enumerate(st[:mid]):
        if e != st[len_ - i - 1]:
            return False
    return True


def solve(line):
    if isPalindrome(line):
        return "yes"
    return "no"


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            return
        ans = solve(line.strip())
        print(ans)


if __name__ == "__main__":
    main()