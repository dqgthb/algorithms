DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    pass


def findMinSum(num): 
    sum = 0

    # Find factors of number 
    # and add to the sum 
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num //= i 
        i += 1
    if num != 1:
        sum += num 
    # Return sum of numbers 
    # having minimum product 
    return sum

def main():
    t = int(input())
    import itertools
    for _ in range(t):
        A, B = (int(i) for i in input().split())

    #for A, B in itertools.product(range(10), range(10)):
        print_("A and B are %d %d" % (A, B))
        minSum = findMinSum(A)
        print_("minSum is %d" % minSum)
        if minSum <= B:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()