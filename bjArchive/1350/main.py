import sys
sys.stdin = open('i', 'r')

def main():
    t = int(input())

    fileSizeList = [inti for i in input().split() if (inti := int(i)) > 0]

    clusterSize = int(input())

    numCluster = 0
    for i in fileSizeList:
        numCluster += ((i-1) // clusterSize + 1)

    totalByte = clusterSize * numCluster

    print(totalByte)




if __name__ == "__main__":
    main()