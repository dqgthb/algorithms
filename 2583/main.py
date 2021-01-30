# CP template Version 1.006
import sys
from collections import deque

ud = [-1, 0, 1, 0]
lr = [0, -1, 0, 1]

input = sys.stdin.readline

m, n, k = map(int, input().split())
mat = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    c -= 1
    d -= 1
    a, b = m - b - 1, a
    c, d = m - d - 1, c
    c, a = a, c
    for i in range(a, c+1):
        for j in range(b, d+1):
            mat[i][j] = 1

area = []
count = 0
for i in range(m):
    for j in range(n):
        if mat[i][j] == 0:
            mat[i][j] = 1
            count = 1
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for dx, dy in zip(ud, lr):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if mat[nx][ny] == 0:
                            count += 1
                            mat[nx][ny] = 1
                            q.append((nx, ny))
            area.append(count)


print(len(area))
area.sort()
sys.stdout.write(' '.join(map(str, *area)))

