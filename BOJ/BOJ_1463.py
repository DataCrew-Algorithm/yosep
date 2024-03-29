# 1463 1로 만들기

n = int(input()) # 14

dp = [0] * (n+1) # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    print(f'i {i}:', dp)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])