# BOJ_4963 섬의 개수
# from collections import deque
# import sys
# read = sys.stdin.readline

# dx = [1, -1, 0, 0, 1, 1, -1, -1]
# dy = [0, 0, -1, 1, 1, -1, 1, -1]
# def bfs(i, j):
#     s[i][j] = 0
#     q = deque()
#     q.append([i, j])
#     while q:
#         a, b = q.popleft()
#         for k in range(8):
#             X = a + dx[k]
#             Y = b + dy[k]
#             if 0 <= X < h and 0 <= Y < w and s[X][Y] == 1:
#                 s[X][Y] = 0
#                 q.append([X, Y])

# ans = []
# while True:
#     w, h = map(int, read().split())
#     if (w, h) == (0, 0):
#         break
#     s = [list(map(int, read().split())) for _ in range(h)]

#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             if s[i][j] == 1:
#                 bfs(i, j)
#                 cnt += 1
#     ans.append(cnt)

# for i in ans:
#     print(i)

# BOJ_4963 섬의 개수
from collections import deque
import sys
read = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        a, b = q.popleft()
        for i in range(8):
            X = a + dx[i]
            Y = b + dy[i]
            if 0 <= Y < h and 0 <= X < w and matrix[Y][X] == 1:
                matrix[Y][X] = 0
                q.append([X, Y])

ans = []
while True:
    w, h = map(int, read().split())
    if (w, h) == (0, 0):
        break
    matrix = [list(map(int, read().split())) for _ in range(h)]
    cnt = 0
    for row in range(h):
        for col in range(w):
            if matrix[row][col] == 1:
                bfs(col, row)
                cnt += 1
    ans.append(cnt)

for i in ans:
    print(i)