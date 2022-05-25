# BOJ 1966 프린터 큐
from collections import deque

for _ in range(int(input())):
    _, target_index = map(int, input().split(" "))
    Queue = deque(map(int, input().split(" ")))
    
    print_out = 0 # 프린트 횟수
    while True:
        if target_index == 0 and Queue[0] == max(Queue):    # 1. 타겟 0번 자리이고 우선도도 가장 높을 때
            print_out += 1                                  #   -> 프린트하고 break
            break
        
        elif target_index == 0 and Queue[0] != max(Queue):  # 2. 타겟 0번 자리이지만 우선도는 낮을 때
            target_index = len(Queue)-1                     #   -> rotate하고 target의 index를 변경
            Queue.rotate(-1)                                
        
        elif Queue[0] == max(Queue):                        # 3. 타겟과 무관하게 우선도가 가장 높을 때
            Queue.popleft()                                 #   -> 프린트하고 한자리씩 앞으로 당기기
            print_out += 1                                  
            target_index -= 1
        
        else:                                               # 4. 출력없음
            Queue.rotate(-1)                                #   -> rotate
            target_index -= 1
    
    print(print_out)