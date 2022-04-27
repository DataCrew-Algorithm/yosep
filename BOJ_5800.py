# 5800 성적 통계

def near_max(list):
    tmp = []
    for i in range(len(list)-1):
        tmp.append(list[i+1]-list[i])
    return max(tmp)

for i in range(int(input())):
    tmp = list(map(int, input().split()))[1:]
    tmp.sort()
    print(f'Class {i+1}\nMax {tmp[-1]}, Min {tmp[0]}, Largest gap {near_max(tmp)}')

# 2
# 5 30 25 76 23 78
# 6 25 50 70 99 70 90

# Class 1
# Max 78, Min 23, Largest gap 46
# Class 2
# Max 99, Min 25, Largest gap 25