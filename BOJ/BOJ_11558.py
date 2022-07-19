# 11558 The Game of Death

T = int(input()) # 케이스 수

def dfs(node):
    for n in graph[node]:
        if called[n] == 0:
            called[n] = 1  
            if n == N: # 호출된 n의 값이 주경이면
                return # 종료
            dfs(n) # 주경이가 나올 때까지 깊이 탐색

for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N+1)] # 케이스 그래프 생성
    called = [0] * (N+1)             # 호출 여부 리스트 생성
    for i in range(N):
        graph[i+1].append(int(input()))
    
    dfs(1)

    # 결과값 출력
    if called[N] == 1:
        print(sum(called))
    else: print(0)