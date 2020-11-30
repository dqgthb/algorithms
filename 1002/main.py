DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    x1, y1, r1, x2, y2, r2 = (int(i) for i in line.split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        return "-1"

    if x1 == x2 and y1 == y2 and r1 != r2:
        return "0"

    distanceSqr = (x1 - x2) ** 2 + (y1 - y2) ** 2
    d = distanceSqr ** (0.5)
    r1r2Sqr = (r1 + r2) ** 2

    C1 = (x1, y1, r1)
    C2 = (x2, y2, r2)

    if r1 < r2:
        tmp = C1
        C1 = C2
        C2 = tmp

    if C1[2] > d + C2[2]:
        return "0"
    elif C1[2] == d + C2[2]:
        return "1"

    if distanceSqr < r1r2Sqr:
        return "2"
    elif distanceSqr == r1r2Sqr:
        return "1"
    else:
        return "0"



def main():
    n = int(input())
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()
