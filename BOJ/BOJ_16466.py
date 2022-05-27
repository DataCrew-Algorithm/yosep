# BOJ 16466 콘서트
from collections import deque

# [실패]deque의 popleft로 작성한 코드 : 런타임 에러 (IndexError)
N = int(input())
sold_tickets = deque(sorted(list(map(int, input().split())))) # 판매된 티켓을 순서대로 정렬
min_ticket = 1  # 비교할 티켓 초기값 지정
while True:
    if min_ticket != sold_tickets[0]:   # sold_tickets이 연속되는 값이면 ex) [1, 2, 3]
        print(min_ticket)               # popleft()에 의해 결국엔 sold_tickets = []이 되고
        break                           # if문의 sold_tickets[0]에서 인덱스 에러 발생
    sold_tickets.popleft()
    min_ticket += 1
                            

# [성공]deque의 rotate로 작성한 코드 : 488ms 
N = int(input())
sold_tickets = deque(sorted(list(map(int, input().split()))))
min_ticket = 1
while True:
    if min_ticket != sold_tickets[0]:
        print(min_ticket)
        break
    sold_tickets.rotate(-1) # popleft 대신에 rotate를 써서 인덱스 에러 방지
    min_ticket += 1