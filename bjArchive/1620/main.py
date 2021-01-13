import os
import sys
import itertools
import collections
TEST = ''
if os.path.exists("i" + TEST):
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input = sys.stdin.readline


def printe(*args,**kwargs):
    print(*args, **kwargs, file=sys.stderr)



def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def main():
    N, M = (int(i) for i in input().split())
    numToName = {}
    nameToNum = {}
    for i in range(1, N+1):
        name = input().strip()
        numToName[i] = name
        nameToNum[name] = i
    
    for i in range(M):
        inpt = input().strip()
        if inpt.isdecimal():
            print(numToName[int(inpt)])
        else:
            print(nameToNum[inpt])


if __name__ == "__main__":
    main()