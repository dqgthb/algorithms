DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
    
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    print("hello world")

def main():


if __name__ == "__main__":
    main()