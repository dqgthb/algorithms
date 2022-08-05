DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(arr):
    arr.sort()
    return arr

def main():
    n = int(input())
    array = [None for _ in range(n)]
    idx = 0
    for line in sys.stdin:
        array[idx] = int(line.strip())
        idx += 1
    
    ans = solve(array)

    for i in ans:
        print(i)

if __name__ == "__main__":
    main()