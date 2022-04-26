# 5635 생일
def get_key(dic, val):
    for key, value in dic.items():
         if val == value:
                 return key

info = {}
for i in range(int(input())):
    tmp = input().split()
    info[tmp[0]] = tmp[3] + tmp[2].zfill(2) + tmp[1].zfill(2)

print(get_key(info, max(info.values())))
print(get_key(info, min(info.values())))