import os
import sys
import itertools
import collections
TEST = ''
if os.path.exists("i" + TEST):
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)


def printe(*args,**kwargs):
    print(*args, **kwargs, file=sys.stderr)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()

dp0 = [1 for _ in range(41)]
dp1 = [1 for _ in range(41)]
dp0[1] = 0
dp1[0] = 0


def main():
    for i in range(2, len(dp0)):
        dp0[i] = dp0[i-1] + dp0[i-2]
        dp1[i] = dp1[i-1] + dp1[i-2]
    
    for _ in range(int(input().strip())):
        n = int(input().strip())
        print(dp0[n], dp1[n])




if __name__ == "__main__":
    main()