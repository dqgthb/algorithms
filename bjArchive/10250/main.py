import os
import sys
DEBUG = False
if os.path.exists("i"):
    DEBUG = True
    sys.stdin = open("i")


def printe(*args, **kwargs):
    import sys
    print(*args, **kwargs, file=sys.stderr)


def solve(line):
    H, W, N = (int(i) for i in line.split())
    n, h = divmod(N-1, H)
    h += 1
    h *= 100
    n += 1
    return h + n


def main():
    t = int(input())
    for _ in range(t):
        line = sys.stdin.readline()
        ans = solve(line.strip())
        print(ans)
    

if __name__ == "__main__":
    main()