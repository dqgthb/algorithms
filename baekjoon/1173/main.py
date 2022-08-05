import enum

class State(enum.Enum):
    Exercise = enum.auto()
    Rest = enum.auto()
    End = enum.auto()

class Workout:

    def __init__(self, N, m, M, T, R):
        self.N = N
        self.m = m
        self.M = M
        self.T = T
        self.R = R
        self.X = m
        self.state = None
        self.minTotal = 0
        self.minExercise = 0

    def choice(self):
        if self.X + self.T <= self.M:
            return State.Exercise
        else:
            return State.Rest
        
    def action(self):
        self.minTotal += 1
        self.state = self.choice()

        if self.state == State.Exercise:
            self.minExercise += 1
            self.X += self.T
        else:
            self.X = max(self.m, self.X - self.R)

    def train(self):
        if self.X + self.T > self.M and self.X == self.m:
            return -1
        while (self.minExercise < self.N):
            self.action()
        return self.minTotal


def main():
    #import sys
    #sys.stdin = open("input.txt", "r")
    inputs = (int(i) for i in input().split())
    workout = Workout(*inputs)
    min_ = workout.train()

    print(min_)


if __name__ == "__main__":
    main()