DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    arr = [int(i) for i in line.split()]
    sumArr = [0 for _ in arr]
    dp(arr, sumArr)
    return max(sumArr)

def dp(arr, sumArr):
    sumArr[0] = arr[0]
    for i in range(1, len(arr)):
        sumArr[i] = max(sumArr[i-1] + arr[i], arr[i])

def main():
    _ = input()
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()