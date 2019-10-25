l = 'hello world hi study make me happy'
i = 0
list=[]
# x = l[-1:-10:-1]
# print(x)
# print(l.split(" ",len(l)))
# list=" ".join(l)
# print(list)
# for x in  l:
#     if (x,l.count(x))  not in list:
#         list.append((x,l.count(x)))
# for h in list:
#     print(h[0],':',h[1])
#

list=[(x,l.count(x)) for x in l if (x,l.count(x)) not in list]
for h in list:
    print(h[0],':',h[1])

