# 3474 교수가 된 현우

# N = int(input())
# result = 0
# cnt = 0
# for i in range((N+1)):
#     cnt += 1
#     if cnt == 6:
#         result += 1
#         cnt = 1
#     if (result+1) % 6 == 0:
#         result += 1
    
# print(cnt)
# print(result)



# 참고

t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    i = 5
    while i <= n:
        cnt += n // i
        i *= 5
    print(cnt)