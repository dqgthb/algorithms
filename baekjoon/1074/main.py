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


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())

cnt = 0
r = 0
c = 0
N = 0
def divideConquer(x, y, n):
    global cnt
    if n == 0: return

    l = 2**n
    mid = l // 2
    numBlock = mid ** 2

    assert x <= r < x + l
    assert y <= c < y + l

    if x <= r < x + mid:
        if y <= c < y + mid:
            divideConquer(x, y, n-1)
        elif y + mid <= c < y + l:
            cnt += numBlock
            divideConquer(x, y+mid, n-1)
        else:
            assert False, "wrong y range"
    elif x + mid <= r < x + l:
        if y <= c < y + mid:
            cnt += 2 * numBlock
            divideConquer(x+mid, y, n-1)
        elif y + mid <= c < y + l:
            cnt += 3 * numBlock
            divideConquer(x+mid, y+mid, n-1)
        else:
            assert False, "wrong y range"
    else:
        assert False, "wrong x mid r l range: %d %d %d %d" % (x, mid, r, l)


def main():
    global cnt, N, r, c
    N, r, c = (int(i) for i in input().split())
    divideConquer(0, 0, N)
    print(cnt)


if __name__ == "__main__":
    main()