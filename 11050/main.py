DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    N, K = (int(i) for i in line.split())

    return binCof(N, K)

def binCof(N, K):
    assert N >= K, "wrong input for binomial coefficient: K (%d) larger than N (%d)" % (K, N)
    print_("calling: ", N, K)
    if K == 0:
        return 1
    if N == K:
        return 1
    return binCof(N-1, K) + binCof(N-1, K-1)

def main():
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()