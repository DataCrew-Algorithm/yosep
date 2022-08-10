# 1057 토너먼트

# 실패
N = int(input())
김지민, 임한수 = map(int, input().split())
cnt_round = 0
members = list(range(1,N+1))
while True:
    cnt_round += 1
    next_round = []
    
    for i in range(1, len(members)+1, 2):
        game_stage = [members[i], members[i+1]]
        if 김지민 in game_stage and 임한수 in game_stage: # 김지민과 임한수가 만난 경우
            print(cnt_round)
            break
        elif game_stage[0] == 김지민 or game_stage[0] == 임한수:
            members

# 해답 : 토너먼트 규칙?
# n, kim, im = map(int, input().split())
# count = 0
# while kim != im: # kim, im가 같아지면 만나게 된 경우이므로 while문 종료
#     kim -= kim // 2
#     im -= im // 2
#     count += 1
# print(count)