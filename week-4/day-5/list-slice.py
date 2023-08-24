"""
to slice array and get new array out of it

"""
a=[54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
b=a[0:5]
c=a[0:8:2]
print(b)
print(c)

# start to end with step of 2
e=a[::2] 
# start to a[3]
f=a[:4]
#from a[2] to a[n-1]
g=a[2:]
print(e)
print(f)
print(g)

#from a[7] to a[2]
h=a[7:1:-1]
# reversing whole list 
i=a[::-1]

j=a[-1::-1]
print(j)
