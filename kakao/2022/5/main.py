def solution(info, edges):
    global G
    global isWolf
    isWolf = info
    N = len(info)
    G = [[] for _ in range(N)]
    for line in edges:
        u, v = line
        G[u].append(v)

    answer = solve(0, 0, 0)
    return answer

def solve(node, sheepNumFromParent):
    if isWolf(node):
        currentSheep = sheepNumFromParent-1
    else:
        currentSheep = sheepNumFromParent+1

    if len(G[node]) == 0:
        return

    elif len(G[node]) > 2:
        left = G[node][0]
        right = G[node][1]

    else:
        left = G[node][0]
        if isWolf[node]:
        solve()









    for child in G[node]:
        if isWolf[child] == 0:
            max_ = max(max_, sheepNum+1)
            max_ = max(max_, solve(child, max_, wolfNum))
        else:
            if sheepNum > wolfNum+1:
                max_ = max(max_, solve(child, sheepNum, wolfNum + 1))
    return max_





def main():
    info = [0,0,1,1,1,0,1,0,1,0,1,1]
    edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    print(solution(info, edges))



if __name__ == "__main__":
    main()