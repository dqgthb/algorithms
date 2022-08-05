class Solution:
    def distance(self, line):
        sIdx = 0
        fIdx = 0
        for i, e in enumerate(line):
            if e == 'S':
                sIdx = i
            elif e == 'F':
                fIdx = i
        return abs(sIdx - fIdx)

print(Solution().distance("....FS..."))