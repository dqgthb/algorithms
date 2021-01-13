DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    nums = [int(i) for i in line.split()]

    count = 0
    for n in nums:
        if isPrime(n):
            count += 1
    return count

def isPrime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    n = input()
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()