import sys


if len(sys.argv) == 1:
    if os.path.isfile("in/i"):
        setStdin("in/i")
    elif os.path.isfile("i"):
        setStdin("i")
sys.stdin = open()
input = sys.stdin.readline  # by default

def solution(t, p):
    #dp = [consult[i][1] for i in range(n)]
    dp = p[:]
    for i in range(n):
        #for j in range(i+consult[i][0],len(consult)):
        for j in range(i + t[i], n):
            #dp[j] = max(dp[j], dp[i] + consult[j][1])
            dp[j] = max(dp[j], dp[i] + p[i])
    # dp 생성 완료 후, T(상담이 걸리는 기간) 을 따져서, 조건을 만족시키는 가장 큰 수를 반환하고자 함
    for i in range(n-1,-1,-1):
        #if consult[i][0] <= n-i: # 현재 인덱스에 해당하는 T 를 더했을때 배열 범위를 벗어나지 않는다면
        if t[i] <= n-i: # 현재 인덱스에 해당하는 T 를 더했을때 배열 범위를 벗어나지 않는다면
            return dp[i]

n = int(input())
consult = []
t = []
p = []
for i in range(n):
    #consult.append(list(map(int,input().split())))
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)
print(consult)
print(t)
print(p)
#print(solution(consult))
print(solution(t, p))