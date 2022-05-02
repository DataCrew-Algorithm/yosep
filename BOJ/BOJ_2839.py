# 경우의 수를 나눠 if문을 사용하여 구현하고자 했으나 실패
# 5로 나눠질 때
# 5와 3으로 나눠질 때
# 3으로만 나눠질 때
# 5와 3으로도 안나눠질 때

# 다른 접근
# 3씩 차감하는 방법(힌트참고함)

    # N = int(input())

    # box_count = 0
    # if N % 5 == 0:
    #     box_count = N // 5

    # elif N // 5 > 0 :  입력 11
    #     for x in range(N // 5, 0, -1):
    #         if (N % (5*x)) % 3 == 0:
    #             box_count = x + (N % (5*x)) // 3
    #             break
    #         elif N % 3 == 0:
    #             box_count = N // 3

    # elif N % 3 == 0:
    #     box_count = N // 3
            
    # else:
    #     box_count = -1
        
    # print(box_count)



#2839 설탕배달
N = int(input())
count = 0 # 봉지 카운트

for _ in range(N // 3):
    if N % 5 == 0: # N을 5로 나눈 나머지가 0이면
        print(count + N // 5)
        N = 0
        break
    
    N -= 3 # N에서 3kg 차감
    count += 1 # 봉지 하나 추가
    if N == 0:
        print(count)

if N > 0: #for문이 끝나서도 나머지가 존재하면
    print(-1)