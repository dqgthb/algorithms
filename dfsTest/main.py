

mat = """
0000101100
1100111100
1111111011
"""

mat = [[int(i) for i in line] for line in mat.split()]


N = 3
M = 10

for i in mat:
    print(i)



DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]

islandSize = 0
def dfs(x, y):
    global islandSize
    mat[x][y] = 1
    islandSize += 1
    for dx, dy in zip(DX, DY):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if mat[nx][ny] == 0:
                dfs(nx, ny)


cnt = 0
islands = []
for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            cnt += 1
            dfs(i, j)
            islands.append(islandSize)
            islandSize = 0

print(cnt)
print(islands)


