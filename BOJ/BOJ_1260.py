# 1260 DFS와 BFS
N, M, V = map(int, input().split())
dic={}
for i in range(N):
    dic[i+1] = set()
for _ in range(M):
    a, b = map(int,input().split())
    dic[a].add(b)
    dic[b].add(a)
# dic = {1: {2, 3}, 2: {1, 5}, 3: {1, 4}, 4: {3, 5}, 5: {2, 4}}

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
            
def bfs(start, dic):
    visited = [start]
    tmp = [start]
    while tmp:
        start = tmp.pop(0)
        for i in dic[start]:
            if i not in visited:
                visited.append(i)
                tmp.append(i)
    return visited
          

visited = [V,]
dfs(V, dic)
print(*visited)


print(*bfs(V, dic))