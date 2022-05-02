# ox퀴즈
"""
loop_count = int(input()) # 5회

for _ in range(loop_count):
    ox = input() # 퀴즈 결과를 str으로 받음
    score = 0 # 총점을 저장할 변수
    before_value = 0 # 연속된 'O' 여부를 확인하기 위한 변수

    for value in ox:
        if value == 'X': # value의 값이 X이면 contnue
            before_value = 0
            continue
        elif value == 'O' and before_value > 0: # 연속된 'O'일 경우
            before_value += 1 # 몇번째 연속되는 값인지
            score += before_value # 그 연속되는 값을 score에 더하기
        else: # 그 외의 모든경우 즉, 'X'바로 다음에 처음으로 'O'가 나오는 경우
            before_value += 1
            score += 1 

    print(score) # 계산된 총합 출력
"""

# 불필요한 코드 수정 ver

# ox퀴즈
loop_count = int(input()) # 5회

for _ in range(loop_count):
    ox = input() # 퀴즈 결과를 str으로 받음
    score = 0 # 총점을 저장할 변수
    O_score = 0 # 연속된 'O'에 점수를 부여

    for value in ox:
        if value == 'X': # value의 값이 X이면
            O_score = 0 # O_score를 0으로 초기
        elif value == 'O': # 연속된 'O'일 경우
            O_score += 1 # 'O'가 연속될 때마다 1씩 추가
            score += O_score # 그 연속되는 값을 score에 더하기

    print(score) # 계산된 총합 출력
