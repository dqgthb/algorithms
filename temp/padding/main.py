sizeOf = {"BOOL": 1, "SHORT": 2, "FLOAT": 4, "INT": 8, "LONG": 16}


def solution(types):
    sizes = []

    buf = [" " for _ in range(len(types) * 16)]

    for type_ in types:
        size = sizeOf[type_]

        sizes.append(size)

    idx = 0
    for size in sizes:
        padding = 8 - (idx % size)
        padding %= 8
        for i in range(idx, idx + padding):
            buf[i] = "."
        idx += padding

        for i in range(idx, idx + size):
            buf[i] = "#"
        idx += size

    buf = "".join(buf).rstrip()

    buf += "." * ((8 - len(buf) % 8) % 8)

    if len(buf) > 128:
        return "HALT"

    ans = []
    temp = ""

    count = 0
    for i, e in enumerate(buf):
        temp += e
        count += 1
        if count == 8:
            ans.append(temp)
            temp = ""
            ans.append(",")
            count = 0
    if temp:
        ans.append(temp)

    ansString = "".join(ans)
    return ansString[:-1]


def main():
    x = ["INT", "INT", "BOOL", "SHORT", "LONG"]
    ret = solution(x)
    print("ret:", ret)
    print()

    x = ["INT", "SHORT", "FLOAT", "INT", "BOOL"]
    ret = solution(x)
    print("ret:", ret)
    print()

    x = ["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]
    ret = solution(x)
    print("ret:", ret)
    print()

    x = [
        "BOOL",
        "LONG",
        "SHORT",
        "LONG",
        "BOOL",
        "LONG",
        "BOOL",
        "LONG",
        "SHORT",
        "LONG",
        "LONG",
    ]

    ret = solution(x)
    print("ret:", ret)
    print()


main()
