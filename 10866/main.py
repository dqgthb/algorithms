import os
import sys
import collections
if os.path.exists("i"):
    sys.stdin = open("i2")
if os.path.exists("a"):
    sys.stdout = open("o", "w")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def print_fast(st, end = "\n"):
    sys.stdout.write(st + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()



def main():
    n = int(input().strip())
    dq = collections.deque()
    for _ in range(n):
        line = input()
        com = line.strip().split()
        c = com[0]
        val = "-1"

        if c == "push_front":
            dq.appendleft(com[1])

        elif c == "push_back":
            dq.append(com[1])

        elif c == "pop_front":
            if len(dq) > 0:
                val = dq.popleft()
            print(val)

        elif c == "pop_back":
            if len(dq) > 0:
                val = dq.pop()
            print(val)

        elif c == "size":
            print(len(dq))

        elif c == "empty":
            print("1" if len(dq) == 0 else "0")

        elif c == "front":
            if len(dq) > 0:
                val = dq[0]
            print_fast(val)

        elif c == "back":
            if len(dq) > 0:
                val = dq[-1]
            print_fast(val)

        else:
            assert False, "wrong input"



if __name__ == "__main__":
    main()