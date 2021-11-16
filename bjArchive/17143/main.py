# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
import itertools
#from itertools import product
#import collections
#from collections import deque, Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global R, C, T, mat, catch, N, M
    R, C, T = map(int, input().split())
    N, M = R, C

    mat = Mat(R, C)

    dir = ((-1, 0), (1, 0), (0, 1), (0, -1)) # UDRL
    for _ in range(T):
        r, c, s, d, z = map(int, input().split())
        r -= 1
        c -= 1
        d -= 1
        mat[r][c] = [s, d, z]

    # ######## INPUT AREA END ############

    catch = 0
    for i in range(C):
        pass
        fishing(i)
        mat = sharkMove()
    print(catch)



def sharkMove():
    newMat = Mat(N, M)
    for i in range(N):
        for j in range(M):
            if mat[i][j] is not None:
                s, d, z = mat[i][j]
                ni = i
                nj = j

                if d == 0: # up
                    q, r = divmod(s+N-1-i, N-1)
                    if q % 2 == 1:
                        mat[i][j][1] = 1
                        ni = r
                        pass
                    else:
                        ni = N-1-r

                elif d == 3: # left
                    q, r = divmod(s+M-1-j, M-1)
                    if q % 2 == 1:
                        mat[i][j][1] = 2
                        nj = r
                        pass
                    else:
                        nj = M-1-r

                elif d == 1: # down
                    q, r = divmod(s+i, N-1)
                    if q % 2 == 0:
                        ni = r
                    else:
                        mat[i][j][1] = 0
                        ni = N-1-r

                elif d == 2: # right
                    q, r = divmod(s+j, M-1)
                    if q % 2 == 0:
                        nj = r
                    else:
                        mat[i][j][1] = 3
                        nj = M-1-r


                if not(newMat[ni][nj] is not None and newMat[ni][nj][2] > z):
                    newMat[ni][nj] = mat[i][j]
                mat[i][j] = None
    return newMat



def fishing(fisherPos):
    global catch
    for i in range(R):
        if mat[i][fisherPos] is not None:
            s, d, z = mat[i][fisherPos]
            catch += z
            mat[i][fisherPos] = None
            return




# TEMPLATE ###############################


enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # by default
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()