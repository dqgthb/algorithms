import sys
import string

for line in sys.stdin:
    line = line.strip()
    lower, upper, digit, blank = 0, 0, 0, 0
    for i in line:
        if i in string.ascii_lowercase:
            lower += 1
        elif i in string.ascii_uppercase:
            upper += 1
        elif i in string.digits:
            digit += 1
        else:
            blank += 1
    print(lower, upper, digit, blank)