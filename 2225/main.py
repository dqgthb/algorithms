import os
import sys
import itertools
import collections

DEBUG = False

def setStdin(f):
    global DEBUG
    global input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
    if os.path.exists("o"):
        sys.stdout = open("o", "w")

    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:

            if os.path.isfile("in/i"):
                setStdin("in/i")

            elif os.path.isfile("i"):
                setStdin("i")

        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])

        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)

def dprint(*args):
    if DEBUG:
        print(*args)

def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)

def ints(): return map(int, sys.stdin.readline().rstrip().split())

class DP():
    def __init__(s, n, k):
        s.n = n
        s.k = k
        s.max_ = 21
        
        dp = [[None for _ in range(s.max_)] for _ in range(s.max_)]
        s.dp =dp
        dp[1][1] = 1
        for i in range(1, len(dp)):
            arr = dp[i]
            arr[1] = 1
            arr[i] = 1
        
        for i in range(3, n):
            for j in range(2, i):
                s.get(i, j)



    def get(s, n, k):
        dp = s.dp
        if dp[n][k] is not None:
            return dp[n][k]
        ret = s.get(n-1, k-1) + s.get(n-1, k)
        dp[n][k] = ret
        return ret


def main(f = None):
    init(f)
    N, K = map(int, input().split())
    dp = DP(N, K)
    ans = dp.get(N, K)
    for i in dp.dp:
        print(i)
    print(ans)

if __name__ == "__main__":
    main()