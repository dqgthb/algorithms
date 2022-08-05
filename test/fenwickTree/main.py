def main():
    min32 = -(1 << 31)
    for x in range(10):
        print(x)
        print(bin32(x))
        print(bin32(x&-x))

def bin32(x):
    x %= 1 << 32
    return '{:32b}'.format(x)

if __name__ == "__main__":
    main()