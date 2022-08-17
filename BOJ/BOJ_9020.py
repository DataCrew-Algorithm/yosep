# 9020 골드바흐의 추측

# 소수 판별 함수
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
    
T = int(input())
for _ in range(T):
    n = int(input())
    left, right = n/2, n/2 # 초기값을 중앙값으로 설정
    while True:
        if isPrime(left) and isPrime(right): # 좌우 모두 다 소수이면
            print(int(left), int(right))
            break
        left -= 1
        right += 1