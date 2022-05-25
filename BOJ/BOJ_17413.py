# 17413 단어 뒤집기 2

# main 함수
def solution(sentence):
    sentence = sentence.replace('<', '*<').replace('>','>*').split('*') # 태그와 태그가 아닌 것으로 나누기
    # >>> 1. <problem>17413<is hardest>problem ever<end>
    # >>> 2. *<problem>*17413*<is hardest>*problem ever*<end>*
    # >>> 3. ['', '<problem>', '17413', '<is hardest>', 'problem ever', '<end>', '']
    result = ''
    for word in sentence:
        if len(word) == 0:  # split으로 생성된 불필요한 공백 무시
            continue
        elif '<' in word:   # 태그는 변경없이 그대로 저장
            result += word
        else:               # 태그를 제외한 문장은 sub함수 적용
            result += reverse_sentence(word) # 
    return result


# sub 함수
def reverse_sentence(sentence):
    sentence = sentence.replace(" ", "* *").split("*") # 문장 속 공백 유지 ex) ['problem', ' ', 'ever']
    sub_result = ''
    for word in sentence:
        if len(word) == 0:  # 공백은 그대로 저장
            sub_result += word
        else:
            tmp = list(word)
            tmp.reverse()
            tmp = "".join(tmp)
            sub_result += tmp
    return sub_result

S =  input()
print(solution(S))