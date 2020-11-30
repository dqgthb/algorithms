DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def solve(line):
    N, M = (int(i) for i in line.split())
    return dp[N][M]



Nlimit = 31
Mlimit = 31
dp = [[ -1 for i in range(Nlimit)] for j in range(Mlimit)]


def printDp():
    print("#\t" * len(dp[0]))
    for arr in dp:
        for i in arr:
            print(str(i)+"\t", end="")
        print()


def buildDp(N = Nlimit, M = Mlimit):
    for i in range(1, M):
        dp[1][i] = i

    for i in range(2, N):
        for j in range(i, M):
            dp[i][j] = sum(dp[i-1][k] for k in range(i-1, j))


def main():
    t = int(input())
    buildDp()
    
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()