import os
import sys
import itertools
import collections

DEBUG = False

def setStdin(f):
    global DEBUG
    global input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
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

def dprint(*args):
    if DEBUG:
        print(*args)

def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)

def ints(): return map(int, sys.stdin.readline().rstrip().split())

def main(f = None):
    init(f)
    t = int(input().strip())
    for _ in range(t):
        k = int(input().strip())
        solve(k)

import heapq
class DEPQ:
    def __init__(self):
        self.minQ = []
        self.maxQ = []
        self.isValid = []
        self.id_ = -1

    def generateId(self):
        self.id_ += 1
        return self.id_
        
    def insert(self, x):
        id_ = self.generateId()
        ele = (x, id_)
        dprint(f"inserting {ele}")
        self.isValid.append(True)
        assert len(self.isValid) == id_ + 1
        heapq.heappush(self.minQ, ele)
        heapq.heappush(self.maxQ, (-x, id_))

    def deleteMax(self):
        dprint("delete Max")
        while self.maxQ:
            val, id_ = heapq.heappop(self.maxQ)
            if self.isValid[id_] == False:
                continue
            else:
                val = -val
                self.isValid[id_] = False
                return
        dprint("nothing to delete")

    def deleteMin(self):
        dprint("delete Min")
        while self.minQ:
            val, id_ = heapq.heappop(self.minQ)
            if self.isValid[id_] == False:
                continue
            else:
                self.isValid[id_] = False
                return
        dprint("nothing to delete")

    def getMin(self):
        while self.minQ:
            val, id_ = heapq.heappop(self.minQ)
            if self.isValid[id_] == False:
                continue
            else:
                return val
        raise "nothing"

    def getMax(self):
        while self.maxQ:
            val, id_ = heapq.heappop(self.maxQ)
            if self.isValid[id_] == False:
                continue
            else:
                return -val
        raise "nothing"

    def getMaxMin(self):
        if not any(self.isValid):
            print("EMPTY")
            return
        else:
            print(self.getMax(), self.getMin())

    def status(self):
        dprint("MINQ:", self.minQ)
        dprint("MAXQ:", self.maxQ)
        dprint("EXST:", self.isValid)

def interpret(dq, cmd, n):
    assert cmd in "DI", "wrong command"
    if cmd == "D":
        assert n in [1, -1], "wrong n"
        if n == 1:
            dq.deleteMax()
        else:
            dq.deleteMin()
    elif cmd == "I":
        dq.insert(n)
    else:
        assert False, "wrong case"

def solve(k):
    dprint("\n##### Test Case\n")
    dq = DEPQ()
    for _ in range(k):
        cmd, n = input().split()
        n = int(n)
        interpret(dq, cmd, n)
        dq.status()
    dq.getMaxMin()




if __name__ == "__main__":
    main()