from sys import stdin
from collections import deque

input = stdin.readline
dir = ((-1, 0), (1, 0), (0, 1), (0, -1))
N, M, K = map(int, input().split())
mat = [list(input().strip()) for _ in range(N)]
S = input().strip()
L = len(S)

dp = [[[0 for _ in range(L)] for _ in range(M)] for _ in range(N)]

dq = deque()
for i in range(N):
    for j in range(M):
        if mat[i][j] == S[-1]:
            dp[i][j][L-1] = 1
            dq.append((i, j, L-1))

cum = 0
while dq:
    i, j, l = dq.popleft()
    if l == 0:
        cum += dp[i][j][l]
        continue

    for di, dj in dir:
        for k in range(1, K+1):
            ni, nj = i + k * di, j + k * dj
            if 0 <= ni < N and 0 <= nj < M:
                if mat[ni][nj] == S[l-1]:
                    if dp[ni][nj][l-1] == 0:
                        dq.append((ni, nj, l-1))
                    dp[ni][nj][l-1] += dp[i][j][l]

print(cum)