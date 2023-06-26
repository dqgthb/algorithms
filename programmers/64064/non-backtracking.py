
def solution(user_id, banned_id):
    global N, cnt, uid, bid, BN
    uid = user_id
    bid = banned_id

    global set_
    
    set_ = set()
    N = len(uid)
    BN = len(bid)
    cnt = 0
    
    lst = []
    visited = [False] * N
    
    dfs(0, lst, visited)
    
    
    return cnt


def dfs(n, lst, visited):
    global cnt
    if n == BN:
        if allMatch(lst):
            tup = tuple(sorted(lst))
            if tup not in set_:
                set_.add(tup)
                cnt += 1
        return
        
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            lst.append(i)
            dfs(n+1, lst, visited)
            lst.pop()
            visited[i] = False
            

def allMatch(lst):    
    return all(match(uid[e], bid[i]) for i, e in enumerate(lst))
    
    # for i, e in enumerate(lst):
    #     if not match(uid[e], bid[i]):
    #         return False
    # return True

def match(x, y):
    return len(x) == len(y) and all(j == '*' or i == j for i, j in zip(x, y))

#     if len(x) != len(y):
#         return False
#     for i, j in zip(x, y):
#         if j != '*' and i != j:
#             return False
#     return True
    
            
        
    