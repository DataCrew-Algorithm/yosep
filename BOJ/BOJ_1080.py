# 1080 - 행렬
from sys import stdin

N, M = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]

# 3 x 3 부분행렬 뒤집기 함수
def flip(i, j): 
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]

cnt = 0
# 확인이 필요한 최소 영역
for i in range(N - 2):  # 행 이동 범위
    for j in range(M - 2):  # 열 이동 범위
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)