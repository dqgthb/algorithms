# CP template Version 1.3
import os
import sys
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter
from math import log, ceil, floor

DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
    if os.path.exists("o"): sys.stdout = open("o", "w")
    if f is not None: setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"): setStdin("in/i")
            elif os.path.isfile("i"): setStdin("i")
        elif len(sys.argv) == 2: setStdin(sys.argv[1])
        else: assert False, "Too many sys.argv: %d" % len(sys.argv)

# Standard IO #
### from io import BytesIO, IOBase
### BUFSIZE = 8192
### class FastIO(IOBase):
###     newlines = 0
###     def __init__(self, file):
###         self._fd = file.fileno()
###         self.buffer = BytesIO()
###         self.writable = "x" in file.mode or "r" not in file.mode
###         self.write = self.buffer.write if self.writable else None
### 
###     def read(self):
###         while True:
###             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
###             if not b:
###                 break
###             ptr = self.buffer.tell()
###             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
###         self.newlines = 0
###         return self.buffer.read()
### 
###     def readline(self):
###         while self.newlines == 0:
###             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
###             self.newlines = b.count(b"\n") + (not b)
###             ptr = self.buffer.tell()
###             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
###         self.newlines -= 1
###         return self.buffer.readline()
### 
###     def flush(self):
###         if self.writable:
###             os.write(self._fd, self.buffer.getvalue())
###             self.buffer.truncate(0), self.buffer.seek(0)
### 
### class IOWrapper(IOBase):
###     def __init__(self, file):
###         self.buffer = FastIO(file)
###         self.flush = self.buffer.flush
###         self.writable = self.buffer.writable
###         self.write = lambda s: self.buffer.write(s.encode("ascii"))
###         self.read = lambda: self.buffer.read().decode("ascii")
###         self.readline = lambda: self.buffer.readline().decode("ascii")
### 
### if sys.version_info[0] < 3:
###     sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
### else:
###     sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
### 
### def print(*args, **kwargs):
###     sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
###     at_start = True
###     for x in args:
###         if not at_start:
###             file.write(sep)
###         file.write(str(x))
###         at_start = False
###     file.write(kwargs.pop("end", "\n"))
###     if kwargs.pop("flush", False):
###         file.flush()
### 
### def inp():
###     return sys.stdin.readline().rstrip("\r\n")  # for fast input
### 
### def ii():
###     return int(inp())
### 
### def si():
###     return str(inp())
### 
### def li(lag = 0):
###     l = list(map(int, inp().split()))
###     if lag != 0:
###         for i in range(len(l)):
###             l[i] += lag
###     return l
### 
### def mi(lag = 0):
###     matrix = list()
###     for i in range(n):
###         matrix.append(li(lag))
###     return matrix
### 
### def lsi(): #string list
###     return list(map(str, inp().split()))
### 
### def printList(a, sep=" "):
###     print(sep.join(map(str, a)))
### # END Standard IO #

# MOD #
class Mod:
    MOD = 10**9 + 7
    maxN = 5
    FACT = [0] * maxN
    INV_FACT = [0] * maxN

    @staticmethod
    def setMOD(n):
        Mod.MOD = n

    @staticmethod
    def add(x, y): return (x+y) % Mod.MOD

    @staticmethod
    def multiply(x, y): return (x*y) % Mod.MOD

    @staticmethod
    def power(x, y):
        if y == 0: return 1
        elif y % 2: return Mod.multiply(x, Mod.power(x, y-1))
        else:
            a = Mod.power(x, y//2)
            return Mod.multiply(a, a)

    @staticmethod
    def inverse(x): return Mod.power(x, Mod.MOD-2)

    @staticmethod
    def divide(x, y): return Mod.multiply(x, Mod.inverse(y))

    @staticmethod
    def allFactorials():
        Mod.FACT[0] = 1
        for i in range(1, Mod.maxN):
            Mod.FACT[i] = Mod.multiply(i, Mod.FACT[i-1])

    @staticmethod
    def inverseFactorials():
        n = len(Mod.INV_FACT)
        Mod.INV_FACT[n-1] = Mod.inverse(Mod.FACT[n-1])
        for i in range(n-2, -1, -1):
            Mod.INV_FACT[i] = Mod.multiply(Mod.INV_FACT[i+1], i+1)

    @staticmethod
    def coeffBinom(n, k):
        if n < k:
            return 0
        return Mod.multiply(Mod.FACT[n], Mod.multiply(Mod.INV_FACT[k], Mod.INV_FACT[n-k]))
    # END Mod #

def dprint(*args):
    if DEBUG: print(*args)

def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

def isStair(n):
    a = list(map(int, str(n)))
    for i in range(len(a)-1):
        x, y = a[i], a[i+1]
        if abs(x - y) != 1:
            return False
    else:
        return True

def main(f = None):
    init(f)
    Mod.setMOD(1000000000)
    n = int(input())
    dp = [[None for _ in range(10)] for _ in range(n+1)]
    for i in range(10):
        dp[1][i] = 1
    for i in range(2, n):
        j = 0
        dp[i][j] = dp[i-1][1]
        for j in range(1, 9):
            dp[i][j] = Mod.add(dp[i-1][j-1], dp[i-1][j+1])
        j = 9
        dp[i][j] = dp[i-1][8]
    print(n)
    print(sum(dp[n]))


if __name__ == "__main__":
    main()