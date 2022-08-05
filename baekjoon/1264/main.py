import sys
sys.stdin = open("input.txt", "r")

def countVowel(text):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0

    for c in text:
        if c in vowels:
            count += 1
    return count

def main():
    while True:
        text = input().lower()
        if text == '#':
            return
        ans = countVowel(text)
        print(ans)


if __name__ == "__main__":
    main()