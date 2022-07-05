# 11403 경로 찾기
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

#플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    for col in row:
        print(col, end = " ")
    print()