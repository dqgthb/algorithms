def solve():
    num = int(input())

    counter = [0 for i in range(26)]

    for _ in range(num):
        c = input()[0]
        counter[ord(c) - ord('a')] += 1

    found = False
    for i, e in enumerate(counter):
        if e >= 5:
            found = True
            print(chr(i + ord('a')), end='')
    
    if not found:
        print("PREDAJA", end = "")



def main():

    import sys
    with open("input.txt", "r") as f:
        sys.stdin = f
        solve()

if __name__ == "__main__":
    main()