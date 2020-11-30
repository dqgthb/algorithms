import sys
sys.stdin = open('i2', 'r')

import collections
import sys
import string

def main():
    text = sys.stdin.read()

    wordList = text.split()
    textWSRemoved = ''.join(wordList)
    freq = collections.Counter(c for c in textWSRemoved)
    max_ = max(freq.values())
    mostFreqChars = [c for c in freq.keys() if freq[c] == max_]
    mostFreqChars.sort()

    print(''.join(mostFreqChars))




if __name__ == "__main__":
    main()