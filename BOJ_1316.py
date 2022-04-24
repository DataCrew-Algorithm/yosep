# 1316 그룹 단어 체커
N = int(input())
count = 0
for _ in range(N):
    text = input()
    for i in range(len(text)):
        if text.find(text[i], i+1, len(text)) - i > 1:  # find를 사용하여 index의 차이가 1이상이면,
            count += 1                                  # 다시말해 같은 문자가 연속되지 않은 위치에서 발견되면 count + 1
            break
print(N-count)