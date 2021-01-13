DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)


def solve(arr, x, y, x2, y2):
    count = 0
    for x_, y_, r in arr:
        dsqr = (x_ - x)**2 + (y_ - y)**2
        dsqr2 = (x_ - x2)**2 + (y_ - y2)**2
        rsqr = r * r

        larger = max(dsqr, dsqr2)
        smaller = min(dsqr, dsqr2)

        if smaller < rsqr < larger:
            count += 1
    return count

def main():
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2 = (int(i) for i in input().split())
        n = int(input())
        arr = [[int(i) for i in input().split()] for _ in range(n)]
        ans = solve(arr, x1, y1, x2, y2)
        print(ans)


if __name__ == "__main__":
    main()