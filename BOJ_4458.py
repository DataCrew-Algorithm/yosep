# 4458 첫 글자를 대문자로

N = int(input())

for _ in range(N):
    words = input()
    print(words.replace(words[0], words[0].upper(), 1)) # 문자의 index 0번자리 문자를 대문자로 replace