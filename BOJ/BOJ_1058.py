# import numpy as np
# # 11403 경로 찾기
# N = int(input())
# graph = []
# for _ in range(N):
#     graph.append(list(input()))
# print(np.array(graph))
# for i, row in enumerate(graph):
#     for j, value in enumerate(row):
#         if value == 'Y':
#             graph[i][j] = 1
#         else:
#             graph[i][j] = 0
# print(np.array(graph))
# #플로이드-워셜 알고리즘
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if graph[i][k] == 1 and graph[k][j] == 1 and i != j:
#                 graph[i][j] = 2

# for row in graph:
#     for col in row:
#         print(col, end = " ")
#     print()

# result_list = []
# for i in graph:
#     result_list.append(len(i) - i.count(0))

# print(max(result_list))



N = int(input())

graph = [list(input()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

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