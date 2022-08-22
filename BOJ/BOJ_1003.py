# 1003 피보나치 함수

def fibonacci(n):
    if n == 0:
#         print("0")
        zero.append(0)
        return 0
    elif n == 1:
#         print("1")
        one.append(1)
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

N = int(input())

for i in range(N):
    zero = []
    one = []
    fibonacci(int(input()))
    print(len(zero), len(one))