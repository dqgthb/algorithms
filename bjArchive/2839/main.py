import sys
#sys.stdin = open('i', 'r')

def solve(w):

    bag3 = 0
    while True:
        a, b = divmod(w, 5)
        if b == 0:
            return a + bag3
        else:
            if w >= 3:
                w -= 3
                bag3 += 1
            else:
                return -1


def main():

    for line in sys.stdin:
        w = int(line)
        ans = solve(w)
        print(ans)

if __name__ == "__main__":
    main()