# 9625 BABBA

K = int(input())
A, B = 1, 0
count_list = [0, 0]
while K > 0:
    count_list[0] = B
    count_list[1] = A + B
    A, B = count_list[0], count_list[1]
    K -= 1
    
print(A, B)