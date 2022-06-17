# 16173 점프왕 쩰리 (Small)

import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    global win
    score = matrix[y][x]
    for dx, dy in [(1, 0), (0, 1)]: # 오른쪽, 아래
        Y, X = y + score*dx, x + score*dy
        if 0 <= Y < N and 0 <= X < N and score != 0:
            if Y == X == N-1:  # (N-1, N-1)에 위치하면
                win = True
                return ;
            dfs(Y, X)
        
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]   # matrix = [[1, 1, 10], [1, 5, 1], [2, 2, -1]]
win = False # 게임 탈출 여부
dfs(0, 0)   # 시작 x, y 좌표
if win:
    print("HaruHaru")
else:
    print("Hing")


# import sys
# sys.setrecursionlimit(10000)

# def dfs(y, x):
#     global ok
#     d = li[y][x]
#     for i, j in [(1, 0), (0, 1)]:
#         Y, X = y + d*i, x+ d*j
#         if 0 <= Y < N and 0 <= X < N and d != 0:
#             if Y == X == N-1:
#                 ok = 1
#                 return ;
#             dfs(Y, X)
        
# N = int(input())
# li = [list(map(int, input().split())) for _ in range(N)]
# ok = 0
# dfs(0, 0)
# print("HaruHaru" if ok else "Hing")