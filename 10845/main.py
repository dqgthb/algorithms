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
class queue:
    @staticmethod
    def push(i):
        buffer.append(i)

    @staticmethod
    def front():
        if len(buffer) > 0:
            print(buffer[0])
        else:
            print(-1)

    @staticmethod
    def back():
        if len(buffer) > 0:
            print(buffer[-1])
        else:
            print(-1)

    @staticmethod
    def pop():
        if len(buffer) > 0:
            print(buffer.pop(0))
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
            queue.push(int(arg))
        elif com == "pop":
            queue.pop()
        elif com == "size":
            queue.size()
        elif com == "empty":
            queue.empty()
        elif com == "front":
            queue.front()
        elif com == "back":
            queue.back()
        else:
            assert "wrong input"



if __name__ == "__main__":
    main()