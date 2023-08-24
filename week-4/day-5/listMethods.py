"""
if i in a:
if i not in b:

to search elemnts in list 
"""
a=[54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
b=[]
for i in a:
    if i not in b:
        b.append(i)

for i in b:
    print(i,a.count(i))