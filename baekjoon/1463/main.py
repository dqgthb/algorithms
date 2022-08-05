import os
import sys
import itertools
import collections
TEST = ''
if os.path.exists("i" + TEST):
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input=sys.stdin.readline


def printe(*args,**kwargs):
    print(*args, **kwargs, file=sys.stderr)


# fast print
def pf(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())




def main():
    X = int(input().strip())
    dp = [0 for _ in range(X+1)]

    for i in range(2, len(dp)):
        o1 = o2 = o3 = 987654321
        if i % 3 == 0:
            o1 = dp[i // 3] + 1
        if i % 2 == 0:
            o2 = dp[i // 2] + 1
        o3 = dp[i - 1] + 1
        dp[i] = min(o1, o2, o3)

    print(dp[X])



if __name__ == "__main__":
    main()