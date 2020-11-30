import os
import sys
if os.path.exists("i"):
    sys.stdin = open("i")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def print_fast(st, end='\n'):
    sys.stdout.write(st + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()


def main():
    n = int(input().strip())
    A = set(get_ints())
    m = int(input().strip())
    B = get_ints()
    for i in B:
        if i in A:
            print_fast("1")
        else:
            print_fast("0")



if __name__ == "__main__":
    main()