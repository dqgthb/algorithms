DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

freq = [0 for _ in range(10001)]

def printFreq(freq):
    
    for i in range(len(freq)):
        num = freq[i]
        while num > 0:
            print(i)
            num -= 1


def main():
    n = int(input())
    for line in sys.stdin:
        i = int(line.strip())
        freq[i] += 1
    printFreq(freq)

if __name__ == "__main__":
    main()