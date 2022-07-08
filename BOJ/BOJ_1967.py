# 1967 트리의 지름
'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
'''

# ver 1 실패
# import sys
# import numpy as np

# N = int(input())

# graph = [[] for _ in range(N+1)]
# score_map = [[0]*(N+1) for _ in range(N+1)]
# print(np.array(score_map))

# for _ in range(N-1):
#     a, b, c  = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     score_map[a][b] = c
#     score_map[b][a] = c

# print(np.array(score_map))
# print(graph)


# import sys
# def dfs(start, end):
#     visited[start] = 1
#     for n in graph[start]:
#         if visited[n] == 0:
#             if n == end:
#                 d += score_map[start][n]
#             else:
#                 dfs(n, end)
#     return ...

# result_list = []

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i == j: continue
#         d = 0
#         visited = [0]*(N+1)
#         d = dfs(i, j)
#         result_list.append(d)


# print(max(result_list))


# ver 2 블로그 참조
# https://kyun2da.github.io/2021/05/04/tree's_diameter/

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))