# 5635 생일
# 1. zfill 함수를 사용하여 day와 month에 0을 추가, 대소 비교가 가능한 생년월일 생성
# 2. 이름(keys)과 생년월일(values)로 구성된 딕셔너리 생성
# 3. value로 key를 반환하는 함수 생성
# 4. 생년월일(value)의 대소관계를 구하고 값에 해당되는 이름(key)를 반환

# value 입력받아 key를 반환하는 함수
def get_key(dic, val):
    for key, value in dic.items():
         if val == value:
                 return key

# 딕셔너리 생성 { 이름 : 생년월일 }
info = {}
for i in range(int(input())):   # 'James 1 1 1991'
    tmp = input().split()       # ['James', '1', '1', '1991']
    info[tmp[0]] = tmp[3] + tmp[2].zfill(2) + tmp[1].zfill(2) # {'James':19910101}
    # info['James'] = '1991' + '01' + '01'

print(get_key(info, max(info.values()))) # 가장 어린 사람
print(get_key(info, min(info.values())))