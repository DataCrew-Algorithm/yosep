# 알파벳 찾기
S =input()
all_alp = 'abcdefghijklmnopqrstuvwxyz'
count_alp = [0]*len(all_alp)  # 길이 26의 문자열 리스트 생성


for alp in all_alp:
    count_alp[all_alp.find(alp)] = S.find(alp) # 각각의 문자열이 몇번째에 위치하는지를 count_alp 리스트에 입력

count_alp = list(map(str, count_alp))
result = ' '.join(count_alp)
print(result)
# result = ''.join(count_alp)
# print(result.split(''))



# ver2
# all_alp = 'abcdefghijklmnopqrstuvwxyz'
# count_alp = ['']*len(all_alp)
# S = input()

# for alp in all_alp:
#     if alp == 'z':
#         count_alp[all_alp.find(alp)] = str(S.find(alp))
#     else:
#         count_alp[all_alp.find(alp)] = str(S.find(alp))+' '
    
# result = ''.join(count_alp)
# print(result)

