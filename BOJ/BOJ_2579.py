# 2579 계단 오르기
N = int(input())
dp = [0] * (N+1)
point = [0] * (N+1)
for i in range(1, N+1):
    point[i] = int(input())
if N==1: # 계단이 1개인 경우
    print(point[1])
elif N==2: # 계단이 2개인 경우
    print(sum(point[:3]))
else: # 계단이 3개 이상인 경우
    dp[1] = point[1]
    dp[2] = point[1]+point[2]
    print(dp)
    for i in range(3, N+1):
        dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i]) # 직전의 계단을 밟지 않았을 경우, 직전의 계단을 밟았을 경우 
        print(point)
        print(dp)
    print(dp[-1])