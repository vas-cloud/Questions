# To Shift '0' At The End Of The Lst Without Touching Non Zero Number

# lst = [0,1,3,0,4,5]
# z_lst = []
# for i in range(len(lst)):
#     if i == 0:
#         z_lst.append(i)
#         lst.pop(lst.index(i))

#         for j in range(len(lst)):
#             if j == 0:
#                 z_lst.append(j)
#                 lst.pop(lst.index(i))

# new_lst = lst + z_lst   
# print(new_lst)


def shift(lst):
    prev = 0
    for i in range(0,len(lst)):
        if lst[i] != 0:
            temp = lst[prev]
            lst[prev] = lst[i]
            lst[i] = temp
            prev+=1
    return lst

lst = [0,1,0,0,4,5,0,7,3,9,0,8,3,0,9,2,4,0]
print(shift(lst))