DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)


def solve(A, B):
    A = int(A.strip())
    B = [int(i) for i in B.strip()]
    for c in reversed(B):
        print(A * c)

    B = int(''.join(str(i) for i in B))
    print(A * B)



def main():
    A = input()
    B = input()
    solve(A, B)

if __name__ == "__main__":
    main()