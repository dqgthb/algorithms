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

s = [False for _ in range(21)]

def main():
    t = int(input().strip())
    for _ in range(t):
        com = input().split()
        if len(com) == 2:
            c, arg = com
            arg = int(arg)
        else:
            c = com[0]

        if c == "add":
            s[arg] = True
        
        elif c == "remove":
            s[arg] = False

        elif c == "check":
            if s[arg]:
                print("1")
            else:
                print("0")
        
        elif c == "toggle":
            s[arg] = not s[arg]
        
        elif c == "all":
            for i in range(len(s)):
                s[i] = True
        
        elif c == "empty":
            for i in range(len(s)):
                s[i] = False
        
        else:
            assert False, "wrong command"




if __name__ == "__main__":
    main()