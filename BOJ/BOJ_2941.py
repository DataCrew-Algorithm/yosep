text = input()
cr_alp = ['-', '=', 'dz', 'lj', 'nj']
del_count = 0

for i in cr_alp:
    del_count += text.count(i)

total_len = len(text) - del_count
print(total_len)


# ver2
# text = input()

# # 크로아티아 문자열 리스트 생성
# cr_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in cr_alp:
#     text = text.replace(i, '*') # 리스트에 해당하는 본문의 문자열을 '*' 대체

# print(len(text)) # 전체 문자열 길이 출력