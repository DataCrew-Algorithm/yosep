# 1149 RGB거리

# 실패
# i번 째 칠한 색의 번호를 객체에 저장하여 i+1번 째 집의 색을 정할 때 겹치지 않게 하고자함
# i번 째 칠한 색 위치를 그대로받아와 i+1번 째 값을 inf로 대체해서 min함수를 이용했을 때 같은 색이 선택되지 않게 함
# 
# import numpy as np
# N = int(input())
# cost = [list(map(int, input().split())) for _ in range(N)]

# result = [0]*3 #
# for i in range(3):
#     tmp_cost = cost.copy()
#     result[i] += tmp_cost[0][i]
#     target_index = i
#     for j in range(1, N):
#         tmp_cost[j][target_index] = np.inf
#         target_index = tmp_cost[j].index(min(tmp_cost[j]))
#         result[i] += min(tmp_cost[j])
# print(min(result))

# 해답 참고
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
print(p)

for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
    print(f'{i}번째 {p}')
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
