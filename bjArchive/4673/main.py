DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def d(n):
    digits = (int(i) for i in str(n))
    return n + sum(digits)

def solve():
    sieve = [False for i in range(10001)]
    for i in range(len(sieve)):
        di = d(i)
        if 0 <= di < len(sieve):
            sieve[d(i)] = True

    for i, e in enumerate(sieve):
        if not e:
            print(i)

def main():
    solve()

if __name__ == "__main__":
    main()