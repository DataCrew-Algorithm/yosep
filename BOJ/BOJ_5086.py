# 5086 배수와 약수

# 잘못된 코드
# for _ in range(3):
#     a, b = map(int, input().split())
#     if b % a == 0:
#         print('factor')
#     elif a % b == 0:
#         print('multiple')
#     else:
#         print('neither')

# input()


# 정답 코드
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif b % a == 0:    # a는 b의 약수
        print('factor')
    elif a % b == 0:    # b는 a의 약수
        print('multiple')
    else:               # 그 외
        print('neither')