# 10994 별 찍기 - 19

N = int(input())
result = ['*']
for _ in range(N-1):
    result.insert(0, '* ' + ' '*len(result[0]) + ' *')
    result.insert(0, '*'*len(result[0]))
    result.append(result[1])
    result.append(result[0])
    for i, line in enumerate(result[2:-2]):
        result[2+i] = '* ' + line + ' *'

for i in result:
    print(i)