# 1406 에디터
# L	    커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	    커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	    커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
#       삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함

import sys

word = list(sys.stdin.readline())
word = word[:-1]
print('init word:', word)
cursor = 0
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    print('order', order)
    if order[0] == 'L' and abs(cursor) != len(word): # 커서를 왼쪽으로 한 칸 옮김, 커서가 맨 앞이면 무시
        cursor -= 1
    elif order[0] == 'D' and cursor != 0: # 커서를 오른쪽으로 한 칸 옮김, 커서가 문장의 맨 뒤이면 무시
        cursor += 1
    elif order[0] == 'B' and abs(cursor) != len(word):
        del word[cursor-1] # 커서 왼쪽에 있는 문자 삭제
    elif order[0] == 'P': # 커서 왼쪽에 입력받은 문자 삽입
        if cursor == 0:
            word.append(order[1])
        else:
            word.insert(cursor, order[1]) 
    print('word:', word)
    print('cursor:', cursor)
        
for n in word:
    print(n, end='')
# print(word, end='')