# 1389 케빈 베이컨의 6단계 법칙
import numpy as np
N, M = map(int, input().split())
INF = float('inf')
arr = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    arr[i][i] = 0
print(np.array(arr))

for _ in range(M):
    a, b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
print(np.array(arr))

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
    print('k', k)
    print(np.array(arr))

score = []
for i in range(1,N+1):
    score.append(sum(arr[i][1:]))
print('score:',score)

print(score.index(min(score))+1)
