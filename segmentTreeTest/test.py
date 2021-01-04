import os
import main
import random

def testCase(testCaseNo = 0):
    x = random.randint(0, 100)
    y = random.randint(0, 100)

    mainResult = main.solve(x, y)
    IknowResult = x+y
    assert mainResult == IknowResult, "wrong!"

def testMain():

    RANDTEST = True
    FILETEST = True

    if RANDTEST:
        random.seed(1)
        for t in range(10):
            print("##### case", t, "#####")
            testCase(t)
            print()
    
    if FILETEST:
        files = os.listdir("in")
        files = sorted(files)

        for f in files:
            print("##### file", f, "#####")
            main.main("in/"+f)
            print()

    print("END SUCCESSFULLY!")


if __name__ == "__main__":
    testMain()