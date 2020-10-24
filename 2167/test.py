import os
import Main2
import random

def createRandomMat(M = 10, N = 10):

    return [[0 for i in range(N+1)]] + \
        [[0] + [random.randint(-10000,10000) for _ in range(N)] for _ in range(M)]


def testCase(testCaseNo = 0):
    M = random.randint(1,10)
    N = random.randint(1,10)

    print("M, N" , M, N)
    mat = createRandomMat(M, N)
    print("mat")
    for i in mat:
        print(i)

    cumMat = Main2.createCumMat(mat)
    print("cumMat")
    for i in cumMat:
        print(i)

    for t in range(2):
        print("testcase", testCaseNo, ": iteration", t)
        i = random.randint(1, M)
        j = random.randint(1, N)
        x = random.randint(i, M)
        y = random.randint(j, N)
        print("i j x y", i, j, x, y)
        ret = Main2.solve(mat, cumMat, i, j, x, y)
        ans = Main2.answer(mat, i, j, x, y)
        assert ret == ans, "something wrong with %d %d" % (ret, ans)
        print(ret)


def main():
    files = os.listdir("in")
    files = sorted(files)
    for f in files:
        print("#####", f, "#####")
        #os.system("python3 main.py in/" + f)
        Main2.main("in/"+f)
        print()

    """
    random.seed(1)

    for t in range(2):
        print("testcase", t)
        testCase(t)
    """


if __name__ == "__main__":
    main()