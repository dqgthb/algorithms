DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i2", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    pass

def isPrime(n):
    if n < 2:
        return False
    i: int = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    M = int(input())
    N = int(input())
    sum_ = 0
    minFound = False
    minPrime = -1

    for i in range(M, N + 1):
        if isPrime(i):
            if not minFound:
                minFound = True
                minPrime = i
            sum_ += i

    if minFound:
        print(sum_)
    print(minPrime)


if __name__ == "__main__":
    main()