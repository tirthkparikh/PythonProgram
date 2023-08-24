# a="Hell tirth"
# print(a.split())
a=1,2,3,4
print(a)

# basicaly this is unpacking or we can say destructing variables from tuple and list
a,b,c,d = 1,2,3,4
print(a)
print(b)
print(c)
print(d)
a,b,c,d = [1,2,3,4]
print(a)
print(b)
print(c)
print(d)


#swapping two values in python
a,b=b,a
print(a,b)


x=[1,2]
y=[3,[4,5]]
zz=x+y
print(zz)
z=[*x,*y]
print(z)

# x,y,z=list(map(int,input().split()))