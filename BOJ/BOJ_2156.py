# 2156 포도주 시식
# 2579 계단 오르기와 비슷하지만 가장 마지막 순서의 포함 여부의 차이점이 존재
N = int(input())
dp = [0] * (N+1)
point = [0] * (N+1)
for i in range(1, N+1):
    point[i] = int(input())
if N==1: # 와인잔이 1개인 경우
    print(point[1])
elif N==2: # 와인잔이 2개인 경우
    print(sum(point[:3]))
else: # 와인잔이 3개 이상인 경우
    dp[1] = point[1]
    dp[2] = point[1]+point[2]
    print(dp)
    for i in range(3, N+1):
        dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i], dp[i-1]) # 직전의 와인잔을 마시지 않았을 경우, 직전의 와인잔을 마셨을 경우, i번째 와인잔을 마시지 않았을 경우 
        print(point)
        print(dp)
    print(max(dp))