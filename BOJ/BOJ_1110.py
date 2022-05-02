# 1110 더하기 사이클
N = int(input())

cycle = 0
tmp = N
while True:
    tmp = 10*(tmp%10) + (tmp//10 + tmp%10)%10
    cycle += 1
    if tmp == N:
        break
print(cycle)