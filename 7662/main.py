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
        self.deleteCounter = 0

    def generateId(self):
        self.id_ += 1
        return self.id_

    def insert(self, x):
        id_ = self.generateId()
        ele = (x, id_)
        dprint(f"inserting {ele}")
        self.isValid.append(True)
        heapq.heappush(self.minQ, ele)
        heapq.heappush(self.maxQ, (-x, id_))
    
    def memoryOptimize(self):
        dprint("##### optimitizing!!")
        minQ = []
        maxQ = []
        isValid = self.isValid[:]
        self.popPushAll(self.minQ, minQ, maxQ, isValid)
        self.popPushAll(self.maxQ, maxQ, minQ, isValid)
        dprint("new q")
        dprint(minQ)
        dprint(maxQ)
        self.minQ = minQ
        self.maxQ = maxQ

        newIds = self.isValid[:]
        counter = 0
        for i, _ in enumerate(newIds):
            if self.isValid[i]:
                newIds[i] = counter
                counter += 1
        for i, e in enumerate(self.minQ):
            x, id_ = e
            self.minQ[i] = (x, newIds[id_])
        for i, e in enumerate(self.maxQ):
            x, id_ = e
            self.maxQ[i] = (x, newIds[id_])
        self.isValid = [True for _ in range(counter)]
        self.id_ = counter-1


    def popPushAll(self, q, q1, q2, isValid):
        while q:
            x, id_ = heapq.heappop(q)
            if isValid[id_]:
                heapq.heappush(q1, (x, id_))
                heapq.heappush(q2, (-x, id_))
                isValid[id_] = False
    
    def deleteValidElement(self, q):
        while q:
            val, id_ = heapq.heappop(q)
            if self.isValid[id_] == False:
                continue
            else:
                self.isValid[id_] = False
                self.deleteCounter += 1
                if self.deleteCounter >= 1:
                    self.deleteCounter = 0
                    self.memoryOptimize()
                return

    def getValidElement(self, q):
        while q:
            val, id_ = heapq.heappop(q)
            if self.isValid[id_] == False:
                continue
            else:
                return val
        raise Exception("no element")

    def getMin(self):
        try:
            return self.getValidElement(self.minQ)
        except:
            pass

    def getMax(self):
        try:
            return -self.getValidElement(self.maxQ)
        except:
            pass

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

def interpret(dq :DEPQ, cmd, n):
    assert cmd in "DI", "wrong command"
    if cmd == "D":
        dprint(f"### deleting {cmd} {n}")
        assert n in [1, -1], "wrong n"
        if n == 1:
            dq.deleteValidElement(dq.maxQ)
        else:
            dq.deleteValidElement(dq.minQ)
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