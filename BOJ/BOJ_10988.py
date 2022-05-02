# 10988 팰린드롬인지 확인하기

word = input()  # 단어 입력
is_palindrome = 1 # 초기값 지정

# 단의 첫글자와 끝글자를 순서쌍으로 비교
for i in range(len(word)//2): # 문자수의 반절만 비교
    if word[i] != word[-(i+1)]: # 맨앞에서 시작한 문자와 맨끝에서 시작한 문자 비교
        is_palindrome = 0 # 비교값이 같지 않다면 0
        break

print(is_palindrome)