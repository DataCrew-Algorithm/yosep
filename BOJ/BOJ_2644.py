# 2644 촌수 계산

# import sys
# def dfs(curr_node):
#     print('curr_node', curr_node)
#     print('connected node:',graph[curr_node])
#     for i in graph[curr_node]:
#         print(f'{curr_node}-{i}')
#         if visited[i] == -1:
#             visited[i] = visited[curr_node] + 1
#             print('visited',visited)
#             dfs(i)
#         print('visited',visited)

# N = int(input())
# graph = [[] for _ in range(int(N+1))]      
# visited = [-1 for _ in range(N+1)]
# print('graph:',graph)
# print('visited:',visited)

# start, end = map(int, input().split())
# for _ in range(int(input())):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# print('graph: ',graph)
# visited[start] = 0
# print('input 1 in start point:', visited)
# dfs(start)
# print(visited[end])




import sys
def dfs(curr_node):
    for i in graph[curr_node]:
        if visited[i] == -1:
            visited[i] = visited[curr_node] + 1
            dfs(i)

N = int(input())
graph = [[] for _ in range(int(N+1))]      
visited = [-1 for _ in range(N+1)]  # start 노드를 기준으로 계산한 촌수를 기록해줄 리스트
                                    # 리스트 요소의 초기값을 -1로 설정
start, end = map(int, input().split())
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited[start] = 0 # 시작지점 자기 자신의 촌수는 0
dfs(start)
print(visited[end])