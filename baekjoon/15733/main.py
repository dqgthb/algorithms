DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    #print(line)
    #return "yes"

    answer = "I'm Sexy"
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))
    # answer = ''.join(list(answer))

    # v (ordinary mouse select)
    # V (line-wise mouse select)
    # ctrl V (box-like mouse select)

    return answer



def main():
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()