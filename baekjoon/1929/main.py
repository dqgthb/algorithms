DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)


def solve(line):
    M, N = (int(i) for i in line.split())
    arr = [0 for _ in range(N+1)]
    arr[1] = 1
    
    for i in range(2, N):
        j = 2
        while i * j <= N:
            arr[i*j] = 1
            j+=1

    for i in range(M, N+1):
        if arr[i] == 0:
            print(i)


def main():
    for line in sys.stdin:
        solve(line)

if __name__ == "__main__":
    main()