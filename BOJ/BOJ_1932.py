# 1932 정수 삼각형
n = int(input())
triangle = [list(map(int, input().split())) for i in range(n)]

# 가장 위층부터 차례대로 덧셈하며 내려가기
for i, floor in enumerate(triangle[:-1]): # 맨 아래층은 제외
    triangle[i+1][0] += floor[0] # 다음 층의 맨 왼쪽 값 채우기  
    triangle[i+1][-1] += floor[-1] # 다음 층의 맨 오른쪽 값 채우기
    for j in range(len(floor)-1): # 양 끝 가장자리를 제외한 값 채우기
        triangle[i+1][j+1] += max(floor[j], floor[j+1])
        
print(max(triangle[-1])) # 누적된 결과값 중 max 출력


# 7 <--- floor
# 10 
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# 7
# 10 15 <---
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# 7
# 10 15
# 18 16 15 <---
# 2 7 4 4
# 4 5 2 6 5

# 7
# 10 15
# 18 16 15
# 20 25 20 19 <---
# 4 5 2 6 5

# 7
# 10 15
# 18 16 15
# 20 25 20 19
# 24 30 27 26 24 <---