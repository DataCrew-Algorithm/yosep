# 1012 유기농 배추

M, N, K = map(int, input().split())
print(M, N, K)

matrix = [[0]*M for i in range(N)]
cabbage_location = []
for _ in range(K):
    x, y = map(int, input().split())
    matrix[y][x] = 1
    cabbage_location.append([[x, y]])

print(matrix)
print(cabbage_location)

for i, location in enumerate(cabbage_location):
    tmp = [[location[0]+1, location[1]], [location[0], location[1]+1], [location[0]-1, location[1]], [location[0], location[1]-1]]
    for j in tmp:
        if j[0] == -1 or j[1] == -1 or j[0] == M or j[1] == N:
            continue
        else:
            cabbage_location[i].append(j)
