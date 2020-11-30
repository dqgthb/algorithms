def input2str():
    str_ = ''
    for _ in range(8):
        str_ += input().strip() + '.'
    return str_

def countF(inputStr):
    count = 0
    for i in range(0, len(inputStr), 2):
        if inputStr[i] == 'F':
            count += 1
    return count

def main():
    #import sys
    #sys.stdin = open("input.txt", "r")
    inputStr = input2str()
    num = countF(inputStr)
    print(num)



if __name__ == "__main__":
    main()