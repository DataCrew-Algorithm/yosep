# 2660 회장뽑기
import numpy as np

N = int(input())
INF = float('inf')

# 배열 생성
arr = [[INF] * (N+1) for _ in range(N+1)] # inf은 무한히 먼사이라는 뜻
for i in range(1,N+1):
    arr[i][i] = 0 # 따라서 자기 자신은 0으로
print(np.array(arr))

# input 값으로 그래프 채우기
while True:
    a,b = map(int,input().split())
    if a==-1 and b==-1:
        break
    arr[a][b] = 1
    arr[b][a] = 1
print(np.array(arr))

# 플로이드–워셜 알고리즘
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
    print('k', k)
    print(np.array(arr))

score = []
for i in range(1,N+1):
    score.append(max(arr[i][1:])) # 친구들의 관계중 가장 큰 수로 count
print('score:',score)

ans_score = min(score) # 가장 작은 score가 회장 후보
candiate_n = score.count(ans_score) # 후보 수 
print(ans_score, candiate_n)
print(*[i+1 for i in range(N) if ans_score==score[i]])

######################################################

# 2660 회장뽑기
import numpy as np

N = int(input())
INF = float('inf')

# 배열 생성
arr = [[INF] * (N) for _ in range(N)]
for i in range(N):
    arr[i][i] = 0 # 자기 자신은 0으로
print(np.array(arr))

# input 값으로 그래프 생성
while True:
    a,b = map(int,input().split())
    if a==-1 and b==-1:
        break
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
print(np.array(arr))

# 플로이드–워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
    print('k', k)
    print(np.array(arr))

score = []
for i in range(N):
    score.append(max(arr[i]))
print('score:',score)

ans_score = min(score)
candiate_n = score.count(ans_score)
print(ans_score, candiate_n)
print(*[i+1 for i in range(N) if ans_score==score[i]])

