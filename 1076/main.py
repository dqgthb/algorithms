class SignalConverter:
    def __init__(self):
        colors = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"
        ]

        value = {}

        val = 0
        for i in colors:
            value[i] = val
            val += 1
        
        mult = {}
        val = 1
        for i in colors:
            mult[i] = val
            val *= 10

        self.colors = colors
        self.value = value
        self.mult = mult

    def convertColor2Value(self, color):
        return self.value[color]

    def convertColor2Mult(self, color):
        return self.mult[color]

    def solve(self, fst, snd, trd):
        d1 = self.convertColor2Value(fst)
        d2 = self.convertColor2Value(snd)
        mult = self.convertColor2Mult(trd)
        d = 10 * d1 + d2 
        d *= mult

        return d



def main():
    converter = SignalConverter()
    fsd = input()
    snd = input()
    trd = input()
    ans = converter.solve(fsd, snd, trd)
    print(ans)

if __name__ == "__main__":
    main()