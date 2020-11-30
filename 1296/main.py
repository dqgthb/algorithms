import sys
sys.stdin = open('i', 'r')

import collections
def solve(name1, name2):
    c1 = collections.Counter(name1)
    c2 = collections.Counter(name2)

    def total(char):
        return c1[char] + c2[char]
    
    L = total("L")
    O = total("O")
    V = total("V")
    E = total("E")

    print(L, O, V, E)
    return ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100

def main():

    name1 = input()
    t = int(input())

    answers = []
    for i in range(t):
        name2 = input()
        answers.append((name2, solve(name1, name2)))

    answers.sort(key = lambda x : x[0])

    print(answers)

    print(max(answers, key = lambda x : x[1])[0])

if __name__ == "__main__":
    main()