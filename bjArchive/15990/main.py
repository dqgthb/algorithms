import os
import sys
import itertools
import collections

DEBUG = False
MOD = 1000000009

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

def dpInit():
    global dp1, dp2, dp3
    dp1= [None for i in range(100001)]
    dp2= [None for i in range(100001)]
    dp3= [None for i in range(100001)]

    for i in range(100001):
        ends1(i)



def ends1(n):
    global dp1, dp2, dp3
    if n < 1:
        return 0
    if n == 1:
        return 1

    if dp1[n] is not None:
        return dp1[n]
    ret = ends2(n-1) + ends3(n-1) 
    ret %= MOD
    dp1[n] = ret
    return ret

def ends2(n):
    global dp1, dp2, dp3
    if n < 2:
        return 0
    if n == 2:
        return 1
    if dp2[n] is not None:
        return dp2[n]
    ret = ends1(n-2) + ends3(n-2) 
    ret %= MOD
    dp2[n] = ret
    return ret

def ends3(n):
    if n < 3:
        return 0
    elif n == 3:
        return 1
    global dp1, dp2, dp3
    if dp3[n] is not None:
        return dp3[n]
    ret = ends1(n-3) + ends2(n-3) 
    ret %= MOD
    dp3[n] = ret
    return ret

def solve(n):
    n1 = ends1(n)
    n2 = ends2(n)
    n3 = ends3(n)
    return sum((n1, n2, n3)) % MOD


def main(f = None):
    init(f)
    T = int(input().strip())
    dpInit()

    for _ in range(T):
        ans = solve(int(input().strip()))
        print(ans)


if __name__ == "__main__":
    main()