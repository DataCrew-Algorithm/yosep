# 14916 거스름돈
n = int(input())

coin_2 = 0
while n >= 0:
    if n % 5 == 0:
        print(n//5 + coin_2)
        break
    n -= 2
    coin_2 += 1
else:
    print(-1)