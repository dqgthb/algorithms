import re


def solution(s):
    s = re.split('(\W)', s)

    for i in range(len(s)):
        s[i] = s[i].capitalize()

    answer = ''.join(s)

    return answer
