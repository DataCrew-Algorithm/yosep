# 1058 친구

N = int(input())
graph = [list(input()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

# 플로이드–워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if graph[i][j]=='Y' or (graph[i][k]=='Y' and graph[k][j]=='Y'):
                visit[i][j] = 1

result = 0
for i in visit:
    result = max(result, sum(i))
print(result)