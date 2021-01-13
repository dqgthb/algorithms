DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    arr = list(line.strip())

    count = 0
    for i,e in enumerate(arr):
        if e == '(':
            count += 1
        elif e == ')':
            count -= 1
            if count < 0:
                return "NO"

    if count == 0:
        return "YES"
    return "NO"


def main():
    n = int(input())
    for line in sys.stdin:
        ans = solve(line)
        print(ans)


if __name__ == "__main__":
    main()