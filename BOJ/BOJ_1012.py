# 1012 유기농 배추

# M, N, K = map(int, input().split())
# print(M, N, K)

# matrix = [[0]*M for i in range(N)]
# cabbage_location = []
# for _ in range(K):
#     x, y = map(int, input().split())
#     matrix[y][x] = 1
#     cabbage_location.append([[x, y]])

# print(matrix)
# print(cabbage_location)

# for i, location in enumerate(cabbage_location):
#     tmp = [[location[0]+1, location[1]], [location[0], location[1]+1], [location[0]-1, location[1]], [location[0], location[1]-1]]
#     for j in tmp:
#         if j[0] == -1 or j[1] == -1 or j[0] == M or j[1] == N:
#             continue
#         else:
#             cabbage_location[i].append(j)


t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            w = a + dx[i]
            q = b + dy[i]
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
                s[q][w] = 0
                queue.append([q, w])
for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            if s[q][w] == 1:
                bfs(w, q)
                s[q][w] = 0
                cnt += 1
    print(cnt)