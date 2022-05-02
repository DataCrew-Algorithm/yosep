def make_set(call_num):
    if hint == 'too high':
        tmp_set = set(num_list[:call_num-1])
    elif hint == 'too low':
        tmp_set = set(num_list[call_num:])
    elif hint == 'right on':
        tmp_set = set([call_num])
    return tmp_set

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
game_log = []
while True:
    tmp = []
    while True:
        call_num = int(input())
        if call_num == 0:
            break
        hint = input()
        tmp.append(make_set(call_num))
        if hint == 'right on':
            break
    if call_num == 0:
        break
    game_log.append(tmp)

print(game_log)
print(len(game_log))
for i in range(len(game_log)):
    for j in game_log[i]:
        if len(game_log[i][-1] & j) != 1:
            print('Stan is dishonest')
            break
else:
    print('Stan may be honest')