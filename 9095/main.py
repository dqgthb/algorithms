DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

dp = [-1 for i in range(11)]


def buildDp():
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for n in range(4, len(dp)):
        dp[n] = dp[n-1] + dp[n-2] + dp[n-3]


def main():
    buildDp()
    _ = input()
    for line in sys.stdin:
        n = int(line.strip())
        print(dp[n])

if __name__ == "__main__":
    main()