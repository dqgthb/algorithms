import os
import sys
import itertools
import collections
TEST = ''
DEBUG = False
if os.path.exists("i" + TEST):
    DEBUG = True
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


N = 0
def stackPush(stack):
    global N
    n = 1
    while True:
        stack.append(n)
        n+=1
        yield


def stackPushFunc(stack):
    stackPushFunc.n += 1
    stack.append(stackPushFunc.n)
stackPushFunc.n = 0


def stackPop(stack: collections.deque):
    return stack.pop()


def main():
    global N
    N = int(input().strip())
    import collections

    stack = []
    push = stackPush(stack)


if __name__ == "__main__":
    main()