# 1929 소수 구하기
# 소수 판별 함수
# ver 1 시간초과
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

start, end = map(int, input().split())
num_list = list(range(start, end+1))
prime_num = []
for i in num_list:
    if is_prime(i) == True:
        prime_num.append(i)
print(*prime_num, sep='\n')


# ver 2 시간초과
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if is_prime(i):
        print(i)


# 해답
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)