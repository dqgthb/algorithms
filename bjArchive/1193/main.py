
def getEleAt(n):
    a = n
    i = 1
    while(a - i > 0):
        a -= i
        i+=1

    a -= 1
    numer = 1 + a
    denom = i - a

    if i % 2 != 0:
        temp = numer
        numer = denom
        denom = temp
    
    return numer, denom

def main():
    n = int(input())
    n, d = getEleAt(n)
    print(n, '/', d, sep ='')


if __name__ == "__main__":
    main()