DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    pass

buffer = []
class stack:
    @staticmethod
    def push(i):
        buffer.append(i)
    
    @staticmethod
    def top():
        if len(buffer) > 0:
            print(buffer[-1])
        else:
            print(-1)

    @staticmethod
    def pop():
        if len(buffer) > 0:
            print(buffer.pop(-1))
        else:
            print(-1)
    
    @staticmethod
    def empty():
        print(0 if len(buffer) > 0 else 1)
    
    @staticmethod
    def size():
        print(len(buffer))

def main():
    t = int(input())
    for line in sys.stdin:
        commands = line.split()
        com = commands[0]
        if len(commands) == 2:
            arg = commands[1]

        if com == "push":
            stack.push(int(arg))
        elif com == "pop":
            stack.pop()
        elif com == "size":
            stack.size()
        elif com == "empty":
            stack.empty()
        elif com == "top":
            stack.top()
        else:
            assert "wrong input"



if __name__ == "__main__":
    main()