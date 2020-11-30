import sys
sys.stdin = open("i", "r")
sys.stdout = open("o", "w")

for line in sys.stdin:
    print(line, end="")