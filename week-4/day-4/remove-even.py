"""
remove all the even numbers from list
"""
a=[56,43,21,58,99,113]

# for i in a:
#     if i%2!=0:
#         b.append(i)
# print(b)

# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)

# for i in b:
#     a.remove(i)

# print(a)


for i in a:
    if i%2==0:
        a.remove(i)
        i-=1
print(a)
