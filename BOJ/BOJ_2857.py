# 2857 FBI

names = []
for _ in range(5):
    names.append(input())

is_FBI = False
for name in names:
    if 'FBI' in name:
        print(names.index(name)+1, end=" ")
        is_FBI = True # FBI 존재
        
if is_FBI == False: # FBI 없음
    print('HE GOT AWAY!')