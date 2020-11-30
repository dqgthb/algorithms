import os
import sys
import itertools
import collections

DEBUG = False
if len(sys.argv) == 1:
    if os.path.exists("i"):
        DEBUG = True
        sys.stdin = open("i")

    if os.path.exists("a"):
        sys.stdout = open("o", "w")

elif len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
else:
    assert False, "too many arguments"
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


def solve():
    iS = input().strip() + "  "
    
    i = 0
    cnt = 0
    l = len(iS) - 2
    while i < l:
        two = iS[i:i+2]
        if iS[i] == 'c':
            if iS[i+1] in set("-="):
                cnt += 1
                i += 2
                continue
        elif iS[i] == 'd':
            if iS[i:i+3] == "dz=":
                cnt += 1
                i += 3
                continue
            elif iS[i+1] == '-':
                cnt += 1
                i += 2
                continue
        elif two == 'lj':
            cnt += 1
            i += 2
            continue
        elif two == 'nj':
            cnt += 1
            i += 2
            continue
        elif two == 's=':
            cnt += 1
            i += 2
            continue
        elif two == 'z=':
            cnt += 1
            i += 2
            continue
        cnt += 1
        i += 1
    print(cnt)

def main():
    for _ in range(4):
        solve()



if __name__ == "__main__":
    solve()