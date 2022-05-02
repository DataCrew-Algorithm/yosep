'''
# 음계
scale = '1 2 3 4 5 6 7 8'
input_scale = input()

if scale == input_scale:
    print('ascending')
elif scale[::-1] == input_scale: # scale[::-1]은 문자열을 반대로 출력
    print('descending')
else:
    print('mixed')

'''
# reversed 사용
scale = list('1 2 3 4 5 6 7 8') # reversed를 사용하기 위해 모든 자료구조를 list로 통일
input_scale = list(input())     #['1', ' ', '2', ' ', '3', ' ', '4', ' ', '5', ' ', '6', ' ', '7', ' ', '8']

if scale == input_scale:
    print('ascending')
elif list(reversed(scale)) == input_scale:  # reveresed를 반드시 list화 해줘야지 '=='로 비교 가능
    print('descending')
else:
    print('mixed')