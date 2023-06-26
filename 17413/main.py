S = input().strip() + " "


isTag = False

ranges = []
start = 0
end = 0
for i, c in enumerate(S):
    if c == "<":
        isTag = True
        end = i
        ranges.append((start, end))

    elif c == ">":
        isTag = False
        start = i + 1

    elif c == " ":
        if not isTag:
            end = i
            ranges.append((start, end))
            start = i + 1


after = list(S)

for s, e in ranges:
    for i in range((e - s) // 2):
        after[s + i], after[e - i - 1] = after[e - i - 1], after[s + i]

print("".join(after))
