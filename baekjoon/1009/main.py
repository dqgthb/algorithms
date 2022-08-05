DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)


dp = [0 for _ in range(22)]
def buildDp(a, m):
    dp[0] = a % m
    for i in range(1, len(dp)):
        dp[i] = (dp[i-1] ** 2) % m


def solve(line):
    a, b = (int(i) for i in line.split())
    m = 10
    a = a % m
    buildDp(a, m)
    mul = 1

    i = 0
    while b != 0:
        if b % 2 == 1:
            mul *= dp[i]
        b >>= 1
        i += 1
    return (mul-1) % m + 1


def main():
    _ = input()
    for line in sys.stdin:
        ans = solve(line)
        print(ans)


if __name__ == "__main__":
    main()