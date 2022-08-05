import re
import itertools

def main():
    p1 = "1 3 2 1 1 3 4 1 6 7"
    p2 = "1 3 2 1 1 3 4 1 6 7 5 9"

    pattern = re.compile(r'\d+ \d+')
    l1 = [[int(i) for i in x.split()] for x in pattern.findall(p1)]
    l2 = [[int(i) for i in x.split()] for x in pattern.findall(p2)]
    l1 = addUpDuplicate(l1)
    l2 = addUpDuplicate(l2)

    print(l1)
    print(l2)

def addUpDuplicate(lst):
    lst.sort()
    newLst = [lst[0]]
    for c, e in itertools.islice(lst, 1, None):
        if e == newLst[-1][1]:
            newLst[-1][0] += c
        else:
            newLst.append([c, e])
    return newLst


def addPolynomial(x, y):

    lx = len(x)
    ly = len(y)

    xc, xe = x[0]
    yc, ye = y[0]


    left, right = 1, 1


    while left < lx and right < ly:
        xc, xe = x[left]
        yc, ye = y[right]
        if xe == ye:













if __name__ == "__main__":
    main()