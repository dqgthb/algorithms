import os
import main
import random

def testCase(testCaseNo = 0):
    pass

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