# 2748 피보나치 수 2
n = int(input())
fbnc_num, sub_num = 0, 1 # 피보나치 수는 0과 1로 시작
fbnc_list = [0, 0] # 수열 생성에 사용할 리스트
while n > 0:
    fbnc_list[0] = sub_num              # index 0은 n 번째 피보나치 수열
    fbnc_list[1] = fbnc_num + sub_num   # index 1은 n+1 번째 피보나치 수열
    fbnc_num, sub_num = fbnc_list[0], fbnc_list[1] 
    n -= 1
    
print(fbnc_num)