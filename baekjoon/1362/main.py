import sys
sys.stdin = open('i', 'r')


class Pet:
    def __init__(self, o, w):
        self.o = o
        self.w = w
        self.isAlive = True

    def getFace(self):
        if self.w <= 0:
            assert not self.isAlive, "not dead"
            return "RIP"
        if self.o / 2 < self.w < 2 * self.o:
            return ":-)"
        return ":-("
    
    def getCommands(self):
        while True:
            input_ = input()
            if input_ == "# 0":
                return self.getFace()

            com, num = input_.split()
            assert com in "EF", "not a valid command"
            num = int(num)
            assert 1 <= num <= 999, "not a valid number"

            if self.isAlive:
                if com == "E":
                    self.w -= num
                else:
                    self.w += num

                if self.w <= 0:
                    self.isAlive = False


def main():

    petCount = 0
    while True:
        input_ = input()
        if input_ == "0 0":
            return

        pet = Pet(*(int(i) for i in input_.split()))
        petCount += 1
        face = pet.getCommands()
        print(petCount, face)


if __name__ == "__main__":
    main()