T = int(input())
for num in range(T):
    a, b = list(map(int, input().split()))
    print(f'Case #{num+1}: {a} + {b} = {a+b}')