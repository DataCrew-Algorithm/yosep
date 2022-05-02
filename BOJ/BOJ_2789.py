# 2789 유학금지

set_alp = 'CAMBRIDGE' # 검열문자열 지정
word = input() 
result = ''

for i in word: # 단어 0위치부터 차례대로 비교
    if i not in set_alp: 
        result += i # 단어에 검열문자가 없다면 result에 차례대로 추가

print(result)