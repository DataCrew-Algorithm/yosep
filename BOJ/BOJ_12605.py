# 12605 단어순서 뒤집기
for i in range(int(input())):
    tmp = input().split()
    tmp.reverse()
    print(f"Case #{i+1}: {' '.join(tmp[::3])}")