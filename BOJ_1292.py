# 1292 쉽게 푸는 문제

def sum_sequence(N): # N번째 자리수까지의 수열의 합을 구하는 함수
    sum_result = 0
    sequence_num = 1 # 1씩 증가시킬 수열, 초기값 = 1
    while N > 0:
        for _ in range(sequence_num): #  '1'은 1번 반복, 2'는 2번반복, 3'은 3번 반복....
            sum_result += sequence_num
            N -= 1
            if N == 0:
                break
        sequence_num += 1 # while문이 한번 반복할 때마다 + 1 씩 증가
    return sum_result


a, b = map(int, input().split())
print(sum_sequence(b) - sum_sequence(a-1))  # a와 b사이의 수열의 합을 sum(a, b)라고 한다면
                                            # sum(a, b) = sum(1, b) - sum(1, a-1)