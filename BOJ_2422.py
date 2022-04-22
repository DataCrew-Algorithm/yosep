# 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 실패

def combination(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combination(array[i+1:], r-1):
                yield [array[i]] + next

N, M = map(int, input().split())
ice_cream = [i for i in range(1, N+1)]

combi = list(combination(ice_cream, 3))

for _ in range(M):
    a, b = map(int, input().split(' '))
    for i in range(len(combi)):
        if a in combi[i] and b in combi[i]:
            combi[i] = []

count = 0
for i in range(len(combi)):
    if bool(combi[i]) == True:
        count += 1

print(count)