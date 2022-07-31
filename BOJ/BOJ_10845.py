# # 10845 큐
# from collections import deque
# lst = deque([])
# for i in range(int(input())):
#     order = input()
#     if len(order) >= 6:
#         _, X = order.split()
#         lst.append(X)
        
#     elif (order == "pop"):
#         if (len(lst) == 0):
#             print(-1)
#         else:
#             print(lst.pop(0))

#     elif (order == "size"):
#         print(len(lst))

#     elif (order == "empty"):
#         if (len(lst) == 0):
#             print(1)
#         else:
#             print(0)

#     elif (order == "front"):
#         if (len(lst) == 0):
#             print(-1)
#         else:
#             print(lst[0])

#     elif (order == "back"):
#         if (len(lst) == 0):
#             print(-1)
#         else:
#             print(lst[-1])

_, X = 'push 1'.split()
print(X)