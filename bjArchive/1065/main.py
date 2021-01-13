DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def isHansu(i):
    if i < 100: return True
    digits = [int(i) for i in str(i)]
    diff = digits[0] - digits[1]

    for i in range(1, len(digits) - 1):
        if digits[i] - digits[i+1] != diff:
            return False
    return True


def solve(line):
    n = int(line.strip())

    if 1 <= n <= 99:
        return n
    
    count = 0
    for i in range(111, n+1):
        if isHansu(i):
            count += 1

    return count + 99


def main():
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()