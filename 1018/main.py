import os
import sys
import itertools
import collections
TEST = ''
if os.path.exists("i" + TEST):
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)


def printe(*args,**kwargs):
    print(*args, **kwargs, file=sys.stderr)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()

WB = tuple("WBWBWBWB")
BW = tuple("BWBWBWBW")


chessWB = (WB, BW, WB, BW, WB, BW, WB, BW)
chessBW = (BW, WB, BW, WB, BW, WB, BW, WB)


M = 0
N = 0
mat = []

def main():
    M, N = (int(i) for i in input().split())
    
    mat = [list(input().strip()) for _ in range(M)]

    min_ = 50 * 50
    for i in range(M - 7):
        for j in range(N - 7):
            caseBw = countDiff88(mat, chessBW, i, j)
            caseWb = countDiff88(mat, chessWB, i, j)
            min_ = min(min_, caseBw, caseWb)

    print(min_)


def countDiff88(mat, chess, x, y):
    count = 0
    for i in range(8):
        for j in range(8):
            if mat[i + x][j + y] != chess[i][j]:
                count += 1
    return count





def printChess88(chess, x, y):
    for i in range(8):
        print(''.join(chess[i+x][y:y+8]))



if __name__ == "__main__":
    main()