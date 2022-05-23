# BOJ 2161 카드1
init_list = list(range(1,int(input())+1)) # 카드 리스트 생성
tmp = [] # 버린 카드 순서대로 저장할 리스트
while len(init_list) > 1: # 남은 카드가 1장이면 반복문 중단
    tmp.append(init_list.pop(0))        # 순서 1 : 가장 위쪽(index 0)카드를 tmp에 저장
    init_list.append(init_list.pop(0))  # 순서 2 : 다음 카드는 기존 리스트의 맨 뒤로 보냄 

print(" ".join(map(str, tmp + init_list))) # join을 적용하기 위해 int -> str로 변환 해줌