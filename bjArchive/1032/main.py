DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(names):
    baseName = names[0]

    pattern = [i for i in baseName]

    otherNames = names[1:]

    for i, e in enumerate(baseName):
        for name in otherNames:
            if name[i] != e:
                pattern[i] = '?'
                break
    return ''.join(pattern)


def findMinSum(num): 
    sum = 0
      
    # Find factors of number 
    # and add to the sum 
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num /= i 
        i += 1
    sum += num 
      
    # Return sum of numbers 
    # having minimum product 
    return sum


def main():
    _ = input()
    fileNames = [i.strip() for i in sys.stdin]
    ans = solve(fileNames)
    print(ans)

if __name__ == "__main__":
    main()