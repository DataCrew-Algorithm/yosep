# 9372 상근이의 여행
# import sys
# for t in range(int(input())):
#     N, M = map(int, input().split())
#     for i in range(M):
#         a, b = map(int, sys.stdin.readline().split())
#     print(N-1)


# dfs
# def dfs(node, count):
#     visited[node] = 1
#     for n in graph[node]:
#         if visited[n] == 0:
#             count = dfs(n, count+1)
#     return count

# for _ in range(int(input())):
#     N, M = map(int, input().split())
#     graph = [[] for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     visited = [0]*(N+1)
#     count = dfs(1, 0)
#     print(count)


import sys
def dfs(node, count):
    visited[node] = 1
    for n in graph[node]:
        if visited[n] == 0:
            count = dfs(n, count+1)
    return count

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0]*(N+1)
    count = dfs(1, 0)
    print(count)