# 3986 좋은 단어
def goodOrBad(x):
    for _ in range(int(len(x))):
        x = x.replace('AA','').replace('BB','')
    if len(x) == 0:
        return 1
    else:
        return 0
        
N = int(input())
count = 0
for _ in range(N):
    count += goodOrBad(input())
print(count)