# 9012 괄호
def yesOrNo(ps):
    stack = []
    for i in range(len(ps)):
        if stack:                    # 스택이 비어있지 않을때,
            if ps[i] != stack[-1]:   # 해당 문자와 스택에 맨 뒤에 문자가 같을 때,
                stack.pop()          # 스택에서 제거
            else:
                stack.append(ps[i]) # 같지 않을 때는 스택에 추가 해줌
        elif len(stack) == 0 and ps[i] == '(':                       # 스택이 비어있을 때
            stack.append(ps[i])     # 스택에 추가
    if not stack:                   # 스택이 비어있으면
        return print('YES')
    else: return print('NO')

for _ in range(int(input())):
    yesOrNo(list(input()))